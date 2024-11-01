import asyncio
import argparse
from pathlib import Path
from crawl4ai import AsyncWebCrawler


async def crawl_and_save(url: str, output_file: str):
    """
    Crawls the specified URL and saves the markdown content to a file.
    Args:
        url: Target website URL to crawl
        output_file: Path to save the markdown content
    Raises:
        ValueError: If no markdown content was retrieved
    """
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(url=url, magic=True)

        if not result.markdown:
            raise ValueError("[ERROR] ❌ No markdown content retrieved from the URL")

        output_path = Path(output_file)
        output_path.write_text(result.markdown, encoding="utf-8")
        print(f"[LOG] 💾 Content saved to: {output_path.absolute()}")


def get_output_filename(url: str) -> str:
    """Prompts user for output filename with a default based on URL"""
    default_name = (
        url.replace("https://", "crawled_")
        .replace("http://", "crawled_")
        .replace("/", "_")
        .strip("._")
        + ".md"
    )

    user_input = input(f"[INPUT] 📝 Enter output filename [{default_name}]: ").strip()
    return user_input if user_input else default_name


def main():
    parser = argparse.ArgumentParser(
        description="Web crawler that saves content to markdown"
    )
    parser.add_argument("url", help="URL to crawl")
    args = parser.parse_args()

    try:
        output_file = get_output_filename(args.url)
        asyncio.run(crawl_and_save(args.url, output_file))
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit(1)


if __name__ == "__main__":
    main()
