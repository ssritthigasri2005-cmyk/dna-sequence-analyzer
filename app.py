import streamlit as st
from Bio.Seq import Seq
import matplotlib.pyplot as plt

st.set_page_config(page_title="DNA Sequence Analyzer", page_icon="🧬")

st.title("🧬 DNA Sequence Analyzer")
st.write("A Bioinformatics tool to analyze any DNA sequence")
st.divider()

dna_input = st.text_area(
    "🔬 Paste your DNA Sequence here:",
    value="ATGCTAGCTAGCTAGCTAGC",
    height=100
)

analyze = st.button("🚀 Analyze!")

if analyze:
    dna_input = dna_input.upper().strip()
    valid = all(base in "ATGC" for base in dna_input)
    if not valid:
        st.error("❌ Invalid! Use only A, T, G, C letters.")
    else:
        dna = Seq(dna_input)
        st.divider()
        st.subheader("📊 Basic Analysis")
        col1, col2, col3 = st.columns(3)
        col1.metric("Length", f"{len(dna)} bp")
        gc = round((dna.count('G') + dna.count('C')) / len(dna) * 100, 2)
        col2.metric("GC Content", f"{gc}%")
        col3.metric("AT Content", f"{round(100-gc, 2)}%")
        st.divider()
        st.subheader("🔁 Sequences")
        st.write("**Complement:**", str(dna.complement()))
        st.write("**Reverse Complement:**", str(dna.reverse_complement()))
        st.write("**mRNA:**", str(dna.transcribe()))
        st.write("**Protein:**", str(dna.transcribe().translate()))
        st.divider()
        st.subheader("📈 Nucleotide Frequency")
        bases = ["A", "T", "G", "C"]
        counts = [dna.count(b) for b in bases]
        colors = ["#4CAF50", "#2196F3", "#FF5722", "#9C27B0"]
        fig, ax = plt.subplots(figsize=(6, 3))
        ax.bar(bases, counts, color=colors)
        ax.set_xlabel("Nucleotide")
        ax.set_ylabel("Count")
        st.pyplot(fig)
        st.divider()
        st.subheader("🥧 GC vs AT Content")
        fig2, ax2 = plt.subplots(figsize=(4, 4))
        ax2.pie(
            [dna.count('G') + dna.count('C'),
             dna.count('A') + dna.count('T')],
            labels=["GC", "AT"],
            colors=["#FF6384", "#36A2EB"],
            autopct="%1.1f%%"
        )
        st.pyplot(fig2)
        st.divider()
        st.success("✅ Analysis Complete!")
