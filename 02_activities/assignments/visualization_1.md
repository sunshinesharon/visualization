# Visualization 1: Number of Services by Location (Python)

### 1. What software did you use to create your data visualization?
I used Python with the libraries `pandas`, `matplotlib`, and `seaborn`.

### 2. Who is your intended audience?
My audience includes policymakers, public health researchers, and digital product teams working in behavioral health.

### 3. What information or message are you trying to convey?
This bar chart highlights the top 15 locations in Ontario by the number of child and youth mental health services. The goal is to visualize regional concentration and potential disparities in access.

### 4. What design principles did you consider?
- **Substantive:** Focused on service distribution by geography.
- **Perceptual:** Used color contrast for easy comparison.
- **Aesthetic:** Kept layout minimal, with clear axis labels and a legible title.

### 5. How did you ensure that your data visualizations are reproducible?
I included a complete, well-commented Python script (`python_code.py`) that can be run with the provided Excel file.

### 6. How did you ensure that your data visualization is accessible?
- Used a clear color palette (Viridis) that’s colorblind-friendly.
- Labelled all axes and ensured the chart can be exported as a high-resolution PNG.

### 7. Who are the individuals and communities who might be impacted by your visualization?
Children, youth, and their families—especially those in underserved areas may benefit from improved service planning based on insights from this data.

### 8. How did you choose which features of your dataset to include or exclude?
I focused on the `MailingAddress1` field as a proxy for location and filtered for the top 15 most frequent addresses to keep the chart clear and actionable.

### 9. What ‘underwater labour’ contributed to your final data visualization product?
- Cleaning column names
- Handling missing data
- Exploring multiple location fields
- Testing various visualizations (bar vs map) before settling on the current version
