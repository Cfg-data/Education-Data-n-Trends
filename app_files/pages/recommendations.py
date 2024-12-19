# pages/recommendations.py

import streamlit as st

def show(data):
    # Title of the page
    st.title("United Nations Policy Recommendations on Advancing Global Education Systems")

    # Introduction
    st.write("""
        **Caveat: Mock UN recommendations created by Ceci for this project as per the analysis done.**
    """)

    st.write("""
        In light of the analysis of global education trends and disparities across regions, the following recommendations are proposed to member states, international organizations, and stakeholders to strengthen educational systems and promote inclusive, equitable, and sustainable education worldwide.
    """)

    # Recommendation 1
    st.write("### 1. **Enhance Educational Data Reporting and Accessibility**")
    st.write("""
        **Recommendation**: Urge member states to adopt standardized and transparent systems for educational data collection and reporting, ensuring consistency across all countries. 
        This will facilitate informed decision-making, strengthen policy planning, and improve tracking of progress in achieving educational goals, particularly in countries with limited data availability.
        
        **Actionable Steps**: Encourage international organizations, such as UNESCO, to provide technical support and capacity-building for data reporting in low-income and conflict-affected regions.
    """)

    # Recommendation 2
    st.write("### 2. **Invest in Teacher Training and Professional Development**")
    st.write("""
        **Recommendation**: Advocate for increased investment in teacher training programs to ensure that educators meet minimum qualification standards, particularly at the secondary education level, 
        with a focus on enhancing the teaching workforce in developing and under-resourced regions.
        
        **Actionable Steps**: Facilitate partnerships between high-income countries and low-income countries to share best practices in teacher training, provide financial incentives for teachers in underserved regions, 
        and promote professional development initiatives.
    """)

    # Recommendation 3
    st.write("### 3. **Address the Digital Divide through Technology Investment**")
    st.write("""
        **Recommendation**: Promote universal access to digital tools and infrastructure, particularly in secondary education, by supporting investment in technology and bridging the digital divide, especially in low-income countries.
        
        **Actionable Steps**: Collaborate with international organizations and the private sector to provide affordable technologies, improve internet connectivity, and support digital literacy programs in underserved areas.
    """)

    # Recommendation 4
    st.write("### 4. **Promote Gender Parity in Secondary and Upper Secondary Education**")
    st.write("""
        **Recommendation**: Strengthen initiatives aimed at reducing gender disparities in secondary and upper secondary education, with a focus on creating safe, inclusive, and accessible learning environments for girls.
        
        **Actionable Steps**: Implement targeted scholarships, mentorship programs, and gender-sensitive educational policies to encourage female enrollment, retention, and completion of secondary and upper-secondary education.
    """)

    # Recommendation 5
    st.write("### 5. **Address Teacher Shortages in Low-Income and Conflict-Affected Regions**")
    st.write("""
        **Recommendation**: Develop policies and initiatives to address teacher shortages, particularly in low-income, conflict-affected, and remote regions. This includes increasing teacher recruitment, providing professional development, and ensuring competitive compensation.
        
        **Actionable Steps**: Work with regional organizations and donor countries to provide targeted financial support, training programs, and incentives to attract and retain teachers in these areas.
    """)

    # Recommendation 6
    st.write("### 6. **Promote Balanced Investment in Education Infrastructure**")
    st.write("""
        **Recommendation**: Encourage member states to allocate a balanced proportion of public education expenditure toward both current operational costs (e.g., staff salaries) and long-term capital investment 
        (e.g., infrastructure, technology, and educational resources).
        
        **Actionable Steps**: Urge international financial institutions and donors to prioritize education infrastructure investments in low- and middle-income countries, especially for the development of modern educational facilities and digital learning environments.
    """)

    # Recommendation 7
    st.write("### 7. **Support Long-Term Strategic Planning for Education Systems**")
    st.write("""
        **Recommendation**: Advocate for the creation of long-term, sustainable education policies that focus on systemic improvements in teacher quality, gender equality, infrastructure, and technology, ensuring resilience to future challenges.
        
        **Actionable Steps**: Encourage governments to develop national education plans that align with international frameworks such as the Sustainable Development Goals (SDGs) and the Education 2030 Agenda.
    """)

    # Recommendation 8
    st.write("### 8. **Facilitate International Collaboration and Knowledge Sharing**")
    st.write("""
        **Recommendation**: Foster global partnerships for knowledge exchange, where countries can share best practices and expertise in addressing common challenges such as teacher shortages, educational inequalities, and digital access gaps.
        
        **Actionable Steps**: Support multilateral platforms for sharing educational research, facilitating peer learning, and scaling successful initiatives, particularly through UN agencies like UNESCO and UNDP.
    """)

    # Recommendation 9
    st.write("### 9. **Develop Targeted Programs for Vulnerable Regions**")
    st.write("""
        **Recommendation**: Design and implement tailored programs that address the specific barriers faced by vulnerable regions, including those affected by economic instability, conflict, or political challenges.
        
        **Actionable Steps**: Mobilize international funding for region-specific education initiatives, such as mobile schools, digital learning platforms, and community-based education solutions.
    """)

    # Recommendation 10
    st.write("### 10. **Enhance International Investment in Education**")
    st.write("""
        **Recommendation**: Urge developed countries and international financial institutions to increase their commitment to financing education, particularly in low-income and conflict-affected regions, 
        in line with international commitments to the SDGs.
        
        **Actionable Steps**: Support the implementation of innovative financing mechanisms, such as education bonds or public-private partnerships, to mobilize additional resources for education.
    """)

    # Conclusion
    st.write("""
        ### Conclusion

        The recommendations above aim to address the critical challenges facing education systems worldwide. 
        By focusing on improving data collection, teacher quality, digital access, gender parity, and infrastructure investment, the international community can advance global educational equity, resilience, and sustainability. 
        The United Nations encourages member states to integrate these recommendations into their national education strategies and to collaborate across borders to achieve inclusive, equitable, and quality education for all.
    """)

    # Call to Action
    st.write("""
        ### Call to Action

        Member states are urged to take immediate action to implement these recommendations, with the support of international organizations, donor countries, and the private sector. 
        The goal is to ensure that every child, regardless of gender, location, or socioeconomic status, has access to high-quality education and the opportunity to reach their full potential.
    """)