import re
from argparse import Namespace
from dataclasses import InitVar, dataclass
from datetime import datetime
from typing import Generator, Union
from urllib.parse import urljoin
import string, hashlib

import asyncio, httpx

class Config:
    """Configuration class"""

    api_url: str = "https://pypi.org/simple/"
    api_package_url: str = "https://pypi.org/pypi/{package_name}/json"
    page_size: int = 2
    sort_by: str = "name"
    date_format: str = "%d-%-m-%Y"
    link_default_format: str = "https://pypi.org/project/{package.name}"

config = Config()

@dataclass
class Package:
    """Package class"""

    name: str
    version: str
    released: str
    description: str
    link: InitVar[str] = None

    def __post_init__(self, link: str = None):
        self.link = link or config.link_default_format.format(package=self)
        self.released_date = datetime.strptime(
            self.released, "%Y-%m-%dT%H:%M:%S%z"
        )

    def released_date_str(self, date_format: str = config.date_format) -> str:
        """Return the released date as a string formatted
        according to date_formate ou Config.date_format (default)

        Returns:
            str: Formatted date string
        """
        return self.released_date.strftime(date_format)

def normalize(name):
    return re.sub(r"[-_.]+", "-", name).lower()

async def search_pypi(query: str):
    async with httpx.AsyncClient(timeout=None, limits=httpx.Limits(max_connections=100)) as client:
        r = await client.get(config.api_url, headers={"accept":"application/vnd.pypi.simple.v1+json"})
        packages = [re.sub(r"\s+", " ", p['name']) for p in r.json()['projects'] if query.lower() in p['name'].lower()]

        tasks = [client.get(config.api_package_url.format(package_name=p)) for p in packages]
        responses = await asyncio.gather(*tasks, return_exceptions=True)

        return [(r.json(), r.url) for r in responses if isinstance(r, httpx.Response) and r.status_code == 200]

async def search(
    query: str, opts: Union[dict, Namespace] = {}
) -> Generator[Package, None, None]:
    """Search for packages matching the query

    Yields:
        Package: package object
    """
    snippets = await search_pypi(query)

    if "sort" in opts:
        if opts.sort == "name":
            snippets = sorted(
                snippets,
                key=lambda s: s[1].path.strip(),
            )
        elif opts.sort == "version":
            from packaging.version import Version

            snippets = sorted(
                snippets,
                key=lambda s: Version(s[0]['info']['version']),
            )
        elif opts.sort == "released":
            snippets = sorted(
                snippets,
                key=lambda s: s[0]['releases'][s[0]['info']['version']][0]['upload_time'] if len(s[0]['releases']) > 0 and len(s[0]['releases'][s[0]['info']['version']]) > 0 else "",
            )

    for PP in snippets:
        (packagesnippets, url) = PP
        package = url.path.replace("/pypi/", "").replace("/json", "")
        if 'message' in packagesnippets and packagesnippets['message'] == 'Not Found': continue
        version = packagesnippets['info']['version']

        releases = packagesnippets['releases']
        if len(releases.keys()) == 0 or len(releases[version]) == 0: continue
        release = releases[version][0]
        
        version = re.sub(
            r"\s+",
            " ",
            version,
        )
        released = re.sub(
            r"\s+",
            " ",
            re.sub(r"\.[0-9]{6}", "", release['upload_time'] + 'Z'),
        )
        description = re.sub(
            r"\s+",
            " ",
            packagesnippets['info']['description'] #.split('\n')[0]
        )
        link = packagesnippets['info']['project_url']

        yield Package(package, version, released, description, link)
