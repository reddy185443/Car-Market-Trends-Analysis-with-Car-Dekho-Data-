# Car Market Trends Analysis with Car Dekho Data

**Student:** MEESALA CHINNA REDDAIAH  
**AICTE STU ID:** STU6a5fa4510cde41784652881

## Project Overview
This project analyzes the supplied Car Dekho dataset to identify patterns in used-car selling prices across manufacturing year, fuel type, seller type, transmission, mileage, ownership and present price.

## Dataset
- Original rows: 301
- Duplicate rows found: 2
- Rows after removing duplicates: 299
- Missing values: 0
- Columns: Car_Name, Year, Selling_Price, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner

## Main Questions
1. How does manufacturing year relate to selling price?
2. Which fuel types have higher average selling prices in this dataset?
3. How do seller type and transmission differ in average selling price?
4. How strongly is present price associated with selling price?
5. Which car models have the highest average selling price?

## Key Findings
- The cleaned dataset contains **299 unique records**.
- Average selling price is **₹4.59 lakh**; median is **₹3.51 lakh**.
- Present price has a strong positive correlation with selling price (**r = 0.88**).
- Diesel cars have a higher average selling price than petrol cars in this dataset (**₹10.10 lakh vs ₹3.26 lakh**).
- Dealer-listed cars have a higher average selling price than individual listings (**₹6.63 lakh vs ₹0.87 lakh**).
- Automatic cars have a higher average selling price than manual cars (**₹9.07 lakh vs ₹3.92 lakh**).
- These group differences are **descriptive, not causal**; the dataset may contain selection and confounding effects.

## Tools & Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

## Project Files
- `analysis.py` — reproducible analysis script
- `Car_Market_Trends_Analysis.ipynb` — notebook version
- `cleaned_car_data.csv` — duplicate-cleaned dataset with derived columns
- `charts/` — generated visualizations
- `DIY_Project_4_Car_Market_Trends_Analysis.pptx` — completed presentation

## How to Run
```bash
pip install -r requirements.txt
python analysis.py
```

For Jupyter:
```bash
jupyter notebook
```

## Important Note
The conclusions describe the **supplied dataset** and should not be interpreted as a current real-world valuation of cars. The data is limited to the records and years present in the CSV.
