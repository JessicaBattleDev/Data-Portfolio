PROJECT: BELLABEAT FITNESS TRACKER ANALYSIS (REFURBISHED)
---------------------------------------------------------
STATUS: Completed
TOOLS: Python (Pandas, Matplotlib, Seaborn)

[PROJECT OVERVIEW]
This project is a complete re-engineering of a legacy analysis originally attempted in R. 
The goal was to build a robust, automated data pipeline to analyze user activity habits.

[THE "WHY"]
I migrated this project from R to Python to improve scalability and automation. 
Unlike the manual ad-hoc analysis, this Python pipeline can:
1. Auto-detect and clean date formats.
2. Standardize column naming conventions automatically.
3. Generate reproducible visualizations with a single click.

[KEY INSIGHTS]
* Data validation confirms a strong positive correlation between Daily Steps and Calories Burned.
* The "Cleaner" module eliminates duplicate records and standardizes time-series data.
* The "Analyst" module generates an executive-summary scatter plot for stakeholders.

[FILE STRUCTURE]
* /Input   - Raw legacy data (Excel/CSV).
* /Scripts - The Python automation modules (Inspector, Cleaner, Analyst).
* /Output  - Cleaned datasets and generated charts.
