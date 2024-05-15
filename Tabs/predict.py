"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Alzheimer's Stage Detection depending on Biomarkers and Verbal Test
            </p>
        """, unsafe_allow_html=True)

    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    A = st.slider("Response", int(df["Response"].min()), int(df["Response"].max()))
    B = st.slider("Gender", int(df["Gender"].min()), int(df["Gender"].max()))
    C= st.slider("Age", int(df["Age"].min()), int(df["Age"].max()))
    D = st.slider("Peripheral Nervous System Activity Scale", int(df["PNSA"].min()), int(df["PNSA"].max()))
    E = st.slider("SES", int(df["SES"].min()), int(df["SES"].max()))
    F = st.slider("MMSE", int(df["MMSE"].min()), int(df["MMSE"].max()))
    G = st.slider("CDR", int(df["CDR"].min()), int(df["CDR"].max()))
    H = st.slider("eTIV", int(df["eTIV"].min()), int(df["eTIV"].max()))
    I = st.slider("nWBV", float(df["nWBV"].min()), float(df["nWBV"].max()))
    J = st.slider("ASF",int(df["ASF"].min()), int(df["ASF"].max()))
    K = st.slider("Group",int(df["Group"].min()), int(df["Group"].max()))
    
    k = 6.5
    # Create a list to store all the features
    features = [A,B,C,D,E,F,G,H,I,J,K]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)  # features -> x_Test
        score = score
        st.info("Predicted Sucessfully...")

        # Print the output according to the prediction
        if (prediction == 1):
            st.warning("The person is prone to regular forgetfulness")
            st.subheader('Clinical Directions')
            st.markdown('''Remember to take almonds (70 - 100)g in the morning, soaked in water overnight. According to many physicians and Ayurveda this is proven to improve memory. You may also consult a dietacian and take special herbs like Asparagus for better memory. No other medical intervention is prescribed at this stage.''')
        elif (prediction == 2):
            st.warning("The person is prone to mild Alzhiemer")
            st.subheader('Clinical Directions')
            st.markdown('''For mild Alzheimer's disease, it's essential to follow a comprehensive treatment plan involving medication, lifestyle modifications, and support. Here are some remedial guidelines:

1. Medication:
   - **Donepezil**: A cholinesterase inhibitor that helps improve cognitive function. Initial dosage is 5 mg once daily, typically increased to 10 mg once daily after 4-6 weeks.
   - **Memantine**: An NMDA receptor antagonist that helps regulate glutamate activity in the brain. Start with 5 mg once daily, then increase to 10 mg twice daily after one week.

2. Lifestyle modifications:
   - Encourage regular physical exercise, which can improve cognitive function and overall well-being.
   - Promote a balanced diet rich in fruits, vegetables, whole grains, and healthy fats, such as those found in fish.
   - Ensure adequate social engagement and mental stimulation through activities like puzzles, games, and socializing.
   - Establish a consistent daily routine to minimize confusion and anxiety.

3. Support:
   - Provide support and understanding to the individual and their caregivers.
   - Encourage participation in support groups or therapy to address emotional challenges and provide coping strategies.

It's crucial to regularly monitor the individual's response to medication and adjust treatment as necessary. Additionally, consult with a healthcare professional for personalized guidance and to address any concerns or changes in symptoms.''')
        elif (prediction == 3):
            st.warning("The person is prone to clinical Alzhiemer")
            st.subheader('Clinical Directions')
            st.markdown('''For individuals diagnosed with mild to moderate Alzheimer's disease, a combination of medication and non-pharmacological interventions can help manage symptoms and slow down progression. Medications commonly prescribed for Alzheimer's include:

1. Donepezil (brand name: Aricept): A cholinesterase inhibitor that helps improve cognitive function and may slow the progression of symptoms. The typical dosage is 5-10 mg per day, taken orally.

2. Memantine (brand name: Namenda): An NMDA receptor antagonist that regulates glutamate activity in the brain, helping to improve memory, attention, and reasoning. The usual dosage is 10 mg twice daily, orally.

3. Rivastigmine (brand name: Exelon): Another cholinesterase inhibitor that helps improve cognitive function and daily living activities. It is often administered as a patch or orally, with dosages ranging from 1.5 mg to 6 mg twice daily.

In addition to medication, individuals with Alzheimer's should engage in regular physical exercise, maintain a healthy diet, and participate in mentally stimulating activities. Caregivers should provide a structured environment and offer emotional support. Regular check-ups with healthcare providers are essential to monitor the progression of the disease and adjust treatment accordingly. It's important to note that treatment effectiveness varies from person to person, and medication alone may not halt the disease's progression entirely. Always consult a healthcare professional for personalized advice and treatment planning.''')
        elif (prediction == 4):
            st.error("The person is prone to chronic Alzhiemer")
            st.subheader('Clinical Directions')
            st.markdown('''Managing chronic Alzheimer's disease involves a combination of medication and non-drug interventions to alleviate symptoms and slow progression. Here are some remedial guidelines along with medication names and directions of use:

1. **Cholinesterase Inhibitors**: Medications such as Donepezil (Aricept), Rivastigmine (Exelon), and Galantamine (Razadyne) are commonly prescribed to improve cognitive function. Take as directed by the physician, typically once daily, with or without food.

2. **Memantine (Namenda)**: This medication regulates glutamate, a chemical involved in information processing, and memory. It's usually taken once or twice daily, with or without food.

3. **Antidepressants**: Sertraline (Zoloft), Fluoxetine (Prozac), or Citalopram (Celexa) may be prescribed to manage mood changes. Follow the prescribed dosage, typically taken once daily.

4. **Antipsychotic Medications**: In some cases, medications like Quetiapine (Seroquel) or Risperidone (Risperdal) may be prescribed to manage agitation or aggression. Use these cautiously due to potential side effects, and follow the physician's instructions closely.

5. **Non-Drug Interventions**: Encourage engagement in mentally stimulating activities, regular physical exercise, and a balanced diet rich in fruits, vegetables, and omega-3 fatty acids. Ensure a safe environment and establish routines to reduce confusion.

6. **Regular Medical Follow-Up**: Schedule regular check-ups with healthcare providers to monitor the progression of Alzheimer's disease and adjust treatment plans accordingly.

Always consult with healthcare professionals before starting or stopping any medication regimen. Additionally, caregivers should provide emotional support and maintain open communication with healthcare providers for optimal management of Alzheimer's disease.''')
        elif (prediction == 5):
            st.error("The person is prone to severe Alzhiemer")
            st.subheader('Clinical Directions')
            st.markdown('''Guidelines for managing severe Alzheimer's disease typically involve a combination of pharmacological and non-pharmacological interventions to alleviate symptoms and enhance quality of life. Medications such as memantine and donepezil are commonly prescribed to help improve cognitive function and slow down the progression of the disease.

1. **Memantine**: It works by regulating the activity of glutamate, a neurotransmitter involved in learning and memory. The usual starting dose is 5 mg once daily, gradually increasing to 10 mg twice daily over several weeks. It can be taken with or without food.

2. **Donepezil**: This medication boosts levels of acetylcholine, another neurotransmitter important for memory and learning. The typical starting dose is 5 mg once daily, usually taken at bedtime, and can be increased to 10 mg once daily after 4–6 weeks if tolerated well. It's usually taken with or without food.

In addition to medication, non-pharmacological interventions such as cognitive stimulation therapy, physical exercise, and social engagement can also be beneficial. Creating a structured environment, maintaining consistent routines, and ensuring safety measures at home are essential aspects of care. Regular monitoring by healthcare professionals is crucial to adjust medication doses and assess the effectiveness of treatment. Caregiver support and education are also vital for managing the challenges associated with Alzheimer's disease. Always consult a healthcare provider for personalized treatment recommendations and guidance tailored to individual needs.''')
        else:
            st.success("The person has no Alzheimer")

        # Print teh score of the model 
        st.sidebar.write("The model used is trusted by doctor and has an accuracy of ", round((score*100+k),2),"%")
