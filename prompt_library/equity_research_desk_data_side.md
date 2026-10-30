# Equity Research Desk - Data Side Prompt

Build the data side of an equity research desk in Python. Model the design on Section 3.1 of Francis & Zhang (2026). Do not include language model roles yet.

### Configuration and Inputs
- Read the environment variable `SEC_USER_AGENT` from the local `.env` file. Send this header with every HTTP request.
- Accept one required command-line argument: `ticker`.
- Accept three optional command-line arguments:
  - `--peers`: a list of peer ticker symbols.
  - `--price`: a numeric stock price.
  - `--step`: a step number to run only one step.
- Do not hardcode any company name in the code.

### Seven Execution Steps
Print the status of each step as it runs.

1. **Step 1: Resolve CIK**
   - Resolve the input ticker to its 10-digit CIK with the SEC `company_tickers.json` file.

2. **Step 2: Identify Filings**
   - Query the SEC EDGAR submissions API for the company filings.
   - Select the latest Form 10-K.
   - Select the latest Form 10-Q.
   - Select the latest Form 8-K that reports Item 2.02 (the earnings release).
   - Print the accession number and the EDGAR "Accepted" timestamp for each selected filing.

3. **Step 3: Download and Extract Text**
   - Download the three selected filings. For the Form 8-K earnings release, download Exhibit 99.1.
   - Convert each document to plain text.
   - Save the plain-text files into a folder named by company identifier, run date, and run time.

4. **Step 4: Extract XBRL Facts**
   - Retrieve the company's XBRL facts JSON from the SEC API.
   - For the latest fiscal year and the prior fiscal year, extract:
     1. Total revenue
     2. Operating income
     3. Net income
     4. Diluted EPS
     5. Stockholders' equity
     6. Long-term debt and its current portion
     7. Cash from operations
     8. Additions to property and equipment
   - For each concept, print the XBRL tag, period end date, and filing reference.
   - If a concept has multiple candidate tags, select the tag with the newest fiscal year.
   - Read every concept for the same fiscal year as revenue. Print the prior-year value beside each figure.

5. **Step 5: Compute Ratios**
   - Compute the following metrics in code and print each calculation with its explicit arithmetic:
     - Revenue growth
     - Operating margin
     - Return on average equity
     - Debt-to-equity ratio (include the current portion of long-term debt)
     - Free cash flow (calculated as cash from operations minus additions to property and equipment)
     - Price-to-Earnings (P/E) ratio (calculated with `--price` if provided)

6. **Step 6: Parse Earnings Release**
   - Search the plain text of the downloaded earnings release.
   - Print the exact lines that report the quarterly total revenue and diluted EPS.

7. **Step 7: Peer Comparison**
   - For each ticker provided in `--peers`, pull the identical XBRL facts.
   - Calculate the operating margin using the exact same tag definition as the primary firm.
   - Save the peer and primary financial facts in the folder beside the plain-text documents.

### Deliverables
- State the exact command to install all required dependencies.
- State the exact command to execute the program with a primary ticker, `--peers`, and `--price`.
