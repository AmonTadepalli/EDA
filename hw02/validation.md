# HW2 Validation — Wildcat Capital Transaction Portfolio

## 2A — Known-Answer Benchmarks

| Check | Expected | Your Script Produced | Match? | Notes |
|---|---|---|---|---|
| Dataset shape | (298772, 9) | (298772, 9) | Yes | |
| Null count — `security_id` | 101,597 | 101,597 | Yes | |
| Null count — `amount` | 0 | 0 | Yes | |
| Unique `txn_type` values | 6 | 6 | Yes | |
| Count of `Buy` transactions | 83,556 | 83,556 | Yes | |
| `txn_date` data type | object | object | Yes | |
| Earliest `txn_date` | 2020-01-01 | 2020-01-01 | Yes | |
| Latest `txn_date` | 2024-12-30 | 2024-12-30 | Yes | |
| Duplicate `txn_id` count | 0 | 0 | Yes | |
| Mean `amount` | $54,075.17 | $54,075.17 | Yes | |
| Median `amount` | $41,220.48 | $41,220.49 | No | 1-cent difference. TODO: investigate — likely a rounding/interpolation difference between pandas' `.median()` on the even-count series vs. how the benchmark was calculated independently. Paste your Cowork investigation here. |
| Skewness of `amount` | 1.15 | 1.15 | Yes | |
| Correlation `shares`–`amount` | 0.65 | 0.65 | Yes | |
| Correlation `price`–`amount` | 0.64 | 0.64 | Yes | |
| Correlation `shares`–`price` | 0.00 | 0.00 | Yes | |
| Negative `shares` count (Buy only) | 836 | 836 | Yes | |
| Profile file created | Yes | Yes | Yes | `hw02/hw02_profile.txt` |
| Chart files created (3) | Yes | Yes | Yes | `hist_amount.png`, `box_amount_by_type.png`, `scatter_shares_amount.png` in `hw02/charts/` |

---

## 2B — Explain the Code and Output

*Complete this section in a NEW Claude Cowork session — not the one that generated the script.*

**Prompt 1 (the code):** [paste hw02_eda.py, then ask: "Walk me through each section of this script, including the grouping, correlation, and charting steps. What should I see in the terminal when I run it? List each expected output value explicitly."]

**Prompt 2 (the output):** [paste the full terminal output, then ask: "Here is the terminal output from running an EDA script on a wealth management transaction dataset. What does each value mean? Flag anything that looks unexpected or that I should investigate before using this data in an analysis."]

1. Did Claude's predicted outputs (from Prompt 1) match what you actually saw in the terminal? List any discrepancies.

   *(your answer here)*

2. What did Claude flag as potentially unexpected or worth investigating (from Prompt 2)?

   *(your answer here)*

3. Did Claude mention the 101,597 null values in `security_id`? What explanation did it give?

   *(your answer here)*

4. Did Claude flag the `txn_date` column as a concern? Why would that matter for a time-series analysis?

   *(your answer here)*

5. Open your three chart files. Does what you see in each image match Claude's explanation of that section of the output? Note any differences.

   *(your answer here)*

6. Paste one follow-up question you asked Claude, and Claude's answer.

   *(your answer here)*

---

## 2C — Business Check & Cross-Validation

**Business-reasonableness questions** (answer in your own words — do not paste Claude's response here):

1. `security_id`, `shares`, and `price` are all null in exactly 101,597 rows. Looking at the `txn_type` value counts, which three transaction types would you expect to have no security — and why? Do the counts add up to 101,597?

   *(your answer here)*

2. There are 83,556 Buy transactions and 59,755 Sell transactions. What does it mean for a wealth management firm to have significantly more Buys than Sells over a five-year period?

   *(your answer here)*

3. The `txn_date` column is stored as a string (type `object`) rather than a date. If Claude Cowork generated code to compute the average number of days between transactions, what would go wrong if the dates remained as strings?

   *(your answer here)*

4. Wildcat Capital has 2,700 clients served by 25 advisors. Is that ratio — roughly 108 clients per advisor — plausible for a registered investment advisory firm?

   *(your answer here)*

5. 836 `Buy` transactions have negative `shares` values (as low as −499.63), while every other transaction type in the dataset has only positive share values. What are two plausible business explanations for a negative share count on a Buy transaction, and what would you do next to determine which explanation is more likely?

   *(your answer here)*

**Cross-validation:**

- Prompt A: "Write Python to count rows in fact_transactions.csv where txn_type equals exactly 'Buy'."
- Prompt B: "Write Python to count the total rows in fact_transactions.csv, then subtract the count of rows where txn_type is Sell, Deposit, Withdrawal, Dividend, or Advisory Fee."

6. What did each script return?

   *(your answer here)*

7. Do the results agree? If not, which one is wrong and why?

   *(your answer here)*

8. Why is it useful to verify a count using subtraction rather than direct filtering?

   *(your answer here)*
