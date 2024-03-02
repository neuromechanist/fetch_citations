# Fetch Citations

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains methods to retrieve citations to NEMAR.org datasets. The methods are implemented in Python and use the __scholarly__ and __scraperAPI__ libraries.

For the best perforce, consider using a paid proxy service such as ScraperAPI.
You can sign up for a free trial at https://www.scraperapi.com/, and then pass your API key to the `get_working_proxy` function.

## Installation

```bash
pip install -e .
```

## Usage

```python
import fetch_citations as fc

# Get citation numbers for a query
cite_count = fc.get_citations_numbers("world peace")
print(count)

# Get citation details for a query
citations = fc.get_citations("world peace", cite_count) # returns a pandas dataframe
print(citations)
citations.to_csv("citations.csv")
```

## Contributing
If you would like to contribute to this project, please open an issue or a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
