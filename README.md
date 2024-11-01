# Web Content Crawler

A simple yet powerful web crawler that extracts content from websites and saves it in markdown format. Built using `crawl4ai` and `playwright-stealth` for reliable web scraping.

## Features

- Asynchronous web crawling for efficient performance
- Automatic content extraction with smart detection
- Markdown output format
- Interactive filename selection
- Error handling and verbose logging
- Stealth mode to avoid detection

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the crawler from the command line:
```bash
python crawl.py <url>
```

Example:
```bash
python crawl.py https://example.com
```

The script will:
1. Prompt for an output filename (with a default suggestion)
2. Crawl the specified URL
3. Extract the content
4. Save it as a markdown file

## Output

The crawler saves the content in markdown format. Output files are named using one of these conventions:
- User-specified filename
- Auto-generated filename based on the URL (e.g., `crawled_example_com.md`)

## Requirements

- Python 3.7+
- crawl4ai
- playwright-stealth
- setuptools

## Error Handling

The script handles various error cases:
- No content found
- Invalid URLs
- Network errors
- File system errors

## License

[MIT License](LICENSE)
