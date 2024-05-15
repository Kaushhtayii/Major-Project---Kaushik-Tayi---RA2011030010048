"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st


def app(df):
    """This function create the Data Info page"""

    # Add title to the page
    st.title("Data Info page")

    # Add subheader for the section
    st.subheader("View Data")

    # Create an expansion option to check the data
    with st.expander("View data"):
        st.dataframe(df,width=1000)
        st.markdown('''
        1. **PNSA -> Peripheral Nervous System Association Score**: This parameter tells how responding is the PNS signal of a human being. The more responsive the PNS electric pulses, the better is the memory and hence lesser chances of Alzheimer.
                    
        2. **SES -> Socio-Economic Status**. This parameter is an indirect measure of the electrode pulses originating from the cognitive and collaborative capabilities of the human brain (right cortex)
                    
        3. **MMSE ->  Mini Mental State Examination**. The combined output of Electrodes which gives a score between 0 to 100. This is regarded as a quantative measurement of cognitive imparement. This is a composite test for orientation to time and place, immediate recall, short-term verbal memory, calculation, language, and construct ability. A score of 23 or less is the generally accepted cutoff point indicating the presence of cognitive impairment.
                    
        4. **CDR -> Clinical Dementia Rating**. Performance is rated in six domains: memory, orientation, judgment and problem solving, community activities, home and hobbies, and personal care Rated on 7 points: 1 = very much improved; 2 = much improved; 3 = minimally improved; 4 = no change; 5 = minimally worse; 6 = much worse; 7 = very much worse. It is more of a verbal interview outcome.
                    
        5. **eTIV -> Estimated Intracranial Volume**. It is a not segmentation-based but calculated from the alignment of the input magnetic resonance (MR) images to the MNI305 brain atlas (i.e. brain imaging from signals.) eTIV and total brain volume for 62 participants were calculated on 1.5-T, T1-weighted MR images using FreeSurfer (version 6.0.0). This parameter is the most effective Biomarker in the test for Alzheimer.
                    
        6. **nWBV -> Normalized Whole Brain Volume**. It is used to to predict incident cognitive impairment and test the cognitive/brain reserve hypothesis. Basically a statistical Biomarker to represent effective volume of the brain that is functional.
                    
        7. **ASF -> Atlas Scaling Factor**. is a one-parameter scaling factor that allows for comparison of the estimated total intracranial volume (eTIV) based on differences in human anatomy. It is defined as the volume-scaling factor required to match each individual to the atlas target. The ASF should be proportional to TIV because atlas normalization equates head size. A validation analysis was performed on 147 subjects to evaluate ASF as a proxy for manual TIV measurement. The scoring of ASF marks the completion of test.
                    
        8. **Group** -> Grouping patients based on cognitive abilities.
                    
        9. **Outcome** -> Definining class of Alzheimer.''')

    # Create a section to columns values
    # Give subheader
    st.subheader("Columns Description:")

    # Create a checkbox to get the summary.
    if st.checkbox("View Summary"):
        st.dataframe(df.describe())

    # Create multiple check box in row
    col_name, col_dtype, col_data = st.columns(3)

    # Show name of all dataframe
    with col_name:
        if st.checkbox("Column Names"):
            st.dataframe(df.columns)

    # Show datatype of all columns 
    with col_dtype:
        if st.checkbox("Columns data types"):
            dtypes = df.dtypes.apply(lambda x: x.name)
            st.dataframe(dtypes)
    
    # Show data for each columns
    with col_data: 
        if st.checkbox("Columns Data"):
            col = st.selectbox("Column Name", list(df.columns))
            st.dataframe(df[col])

    # Add the link to you dataset
    st.markdown("""
                    <p style="font-size:24px">
                        <a 
                            href="https://www.kaggle.com/datasets/brsdincer/alzheimer-features"
                            target=_blank
                            style="text-decoration:none;"
                        >Get Dataset
                        </a> 
                    </p>
                """, unsafe_allow_html=True
    )
    with st.expander('Understanding the parameters'):
        st.markdown('''
        1. PNSA -> Peripheral Nervous System Association Score: This parameter tells how responding is the PNS signal of a human being. The more responsive the PNS electric pulses, the better is the memory and hence lesser chances of Alzheimer.
                    
        2. SES -> Socio-Economic Status. This parameter is an indirect measure of the electrode pulses originating from the cognitive and collaborative capabilities of the human brain (right cortex)
                    
        3. MMSE ->  Mini Mental State Examination. The combined output of Electrodes which gives a score between 0 to 100. This is regarded as a quantative measurement of cognitive imparement. This is a composite test for orientation to time and place, immediate recall, short-term verbal memory, calculation, language, and construct ability. A score of 23 or less is the generally accepted cutoff point indicating the presence of cognitive impairment.
                    
        4. CDR -> Clinical Dementia Rating. Performance is rated in six domains: memory, orientation, judgment and problem solving, community activities, home and hobbies, and personal care Rated on 7 points: 1 = very much improved; 2 = much improved; 3 = minimally improved; 4 = no change; 5 = minimally worse; 6 = much worse; 7 = very much worse. It is more of a verbal interview outcome.
                    
        5. eTIV -> Estimated Intracranial Volume. It is a not segmentation-based but calculated from the alignment of the input magnetic resonance (MR) images to the MNI305 brain atlas (i.e. brain imaging from signals.) eTIV and total brain volume for 62 participants were calculated on 1.5-T, T1-weighted MR images using FreeSurfer (version 6.0.0). This parameter is the most effective Biomarker in the test for Alzheimer.
                    
        6. nWBV -> Normalized Whole Brain Volume. It is used to to predict incident cognitive impairment and test the cognitive/brain reserve hypothesis. Basically a statistical Biomarker to represent effective volume of the brain that is functional.
                    
        7. ASF -> Atlas Scaling Factor. is a one-parameter scaling factor that allows for comparison of the estimated total intracranial volume (eTIV) based on differences in human anatomy. It is defined as the volume-scaling factor required to match each individual to the atlas target. The ASF should be proportional to TIV because atlas normalization equates head size. A validation analysis was performed on 147 subjects to evaluate ASF as a proxy for manual TIV measurement. The scoring of ASF marks the completion of test.
                    
        8. Group -> Grouping patients based on cognitive abilities.
                    
        9. Outcome -> Definining class of Alzheimer.
                    ''')