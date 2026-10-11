import os
from dotenv import load_dotenv
from exa_py import Exa

load_dotenv()

exa = Exa(os.getenv("EXA_API_KEY"))


def search_web(query):
    social_domains = [
        "instagram.com",
        "x.com",
        "youtube.com",
        "facebook.com",
        "reddit.com",
        "pinterest.com"
    ]

    results_by_platform = []

    for domain in social_domains:
        response = exa.search(
            query,
            num_results=3,
            type="auto",
            include_domains=[domain]
        )

        platform_results = []

        for result in response.results:
            platform_results.append({
                "title": result.title or "Untitled result",
                "url": result.url
            })

        results_by_platform.append(platform_results)

    # Take one result from each platform in turn
    results = []
    seen_urls = set()

    for index in range(2):
        for platform_results in results_by_platform:
            if index < len(platform_results):
                result = platform_results[index]

                if result["url"] not in seen_urls:
                    seen_urls.add(result["url"])
                    results.append(result)

                if len(results) == 6:
                    return results

    return results