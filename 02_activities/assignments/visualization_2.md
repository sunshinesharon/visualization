## Visualization 2: Youth Mental Health Services by Age (Tableau)

**Tool Used:** Tableau Public  
**Audience:** Youth program directors, digital health product teams, and policymakers  
**Message:** This visualization shows which youth age groups are most targeted by available mental health services in Ontario.

**Link to interactive visualization:**  
👉 [View on Tableau Public](https://public.tableau.com/app/profile/sharon.jacob5156/viz/YouthMentalHealthServicesbyAge/YouthMentalHealthServicesbyAgeOntario?publish=yes)

**Design Notes:**  
- A treemap was chosen to show proportional focus across age groups.
- Split fields were used to clean the age data and isolate meaningful categories.

**Reproducibility & Accessibility:**  
- Tableau workbook steps are saved in `tableau_steps.txt`
- The link is public; a static image is also available in the repo.

**Question Responses**
### 1. What software did you use to create your data visualization?
I used **Tableau Public** to create this interactive visualization. Tableau enabled me to quickly split and manipulate semicolon-separated age data from the dataset, allowing for an intuitive treemap display that highlights how services are distributed across different youth age groups.

### 2. Who is your intended audience?
My intended audience includes:
- **Youth mental health service planners and policymakers** looking to assess age-specific gaps.
- **Product managers and researchers** working on digital or AI-based solutions (like Live AI or Train AI at Curajoy) to support underserved age groups.
- **Community organizations and advocacy groups** focused on improving equitable access to services.

### 3. What information or message are you trying to convey with your visualization?
The message I want to convey is that **certain age groups—particularly teens and young adults—are more frequently targeted by mental health services**, while others may be less represented. This insight helps inform both policy decisions and the design of AI products that adapt based on user age and developmental needs.

### 4. What design principles (substantive, perceptual, aesthetic) did you consider?
- **Substantive:** Focused on breaking down `Custom_Eligibility by Age` to uncover real patterns in service eligibility.
- **Perceptual:** Used a **treemap**, which is excellent for comparing parts-to-whole and visualizing proportional focus.
- **Aesthetic:** Chose a clean, readable color palette with sufficient contrast; added a clear title; limited data labels to maintain clarity.


### 5. How did you ensure that your data visualizations are reproducible?
The process steps are included in a `tableau_steps.txt` file in this repository. The dataset (`.xlsx`) is provided, and the chart is publicly viewable via Tableau Public at the link below:

👉 [View Tableau Visualization](https://public.tableau.com/app/profile/sharon.jacob5156/viz/YouthMentalHealthServicesbyAge/YouthMentalHealthServicesbyAgeOntario?publish=yes)

### 6. How did you ensure that your data visualization is accessible?
- I used high-contrast colors and a layout that is screen-friendly.
- Data values are represented visually and textually for screen readers.
- The treemap is published on Tableau Public, which supports responsive design and is mobile accessible.

### 7. Who are the individuals and communities who might be impacted by your visualization?
The most directly impacted communities are:
- **Youth and caregivers** navigating mental health services in Ontario
- **Policy and program designers** deciding which age groups to prioritize

### 8. How did you choose which features of your chosen dataset to include or exclude from your visualization?
I focused solely on the `Custom_Eligibility by Age` field, which was the most relevant for understanding the service landscape by age. Other fields like gender or service type were excluded to maintain focus and clarity.

### 9. What ‘underwater labour’ contributed to your final data visualization product?
- Cleaning and splitting age ranges stored as semicolon-separated values.
- Experimenting with multiple chart types before deciding on a treemap.
- Adjusting Tableau formatting for accessibility and usability.
- Testing multiple export versions for optimal screenshot and link-based viewing.
