import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

st.set_page_config(page_title="Carbon-14 Decay Simulator", page_icon="⚛️", layout="wide")

st.markdown("""
<style>
.stApp {background-color:#F4F7FB;}
.block-container {padding-top:2rem; padding-bottom:3rem; max-width:1200px;}
.hero {background:linear-gradient(120deg,#102A43,#176B87); padding:35px;
       border-radius:18px; color:white; margin-bottom:25px;}
.hero-label {color:#7DD3FC; font-size:13px; letter-spacing:3px; font-weight:bold;}
.hero h1 {color:white; font-size:38px; margin:12px 0;}
.hero p {color:#D9EAF7; font-size:16px;}
.section-title {color:#12344D; font-size:22px; font-weight:700; margin-top:20px; margin-bottom:12px;}
.info-card {background:white; padding:20px; border-radius:14px;
            border:1px solid #E1E8F0; margin-bottom:12px;}
.small-note {color:#64748B; font-size:13px;}
</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown("""
<div class="hero">
    <div class="hero-label">MATHEMATICAL MODELING PROJECT</div>
    <h1>⚛️ Carbon-14 Decay Simulator</h1>
    <p>Simulasi peluruhan radioaktif untuk memperkirakan usia sampel organik
    menggunakan Persamaan Diferensial Orde Satu.</p>
    <hr style="border-color:#527D98;">
    <span>PYTHON</span> &nbsp; • &nbsp; <span>STREAMLIT</span> &nbsp; • &nbsp;
    <span>RADIOACTIVE DECAY</span>
</div>
""", unsafe_allow_html=True)
st.write("Aplikasi pembelajaran untuk memahami hubungan antara waktu, jumlah Karbon-14 yang tersisa, dan usia sampel.")

# MODEL KARBON-14
waktu_paruh = 5730.0
k = math.log(0.5) / waktu_paruh

# 01 INPUT
st.markdown('<div class="section-title">01 / Parameter Simulasi</div>', unsafe_allow_html=True)
kolom_input, kolom_info = st.columns([1.2, 1])
with kolom_input:
    persentase = st.slider(
        "Persentase Karbon-14 yang tersisa", min_value=1, max_value=100,
        value=25, step=1, format="%d%%",
        help="Persentase input simulasi dibandingkan jumlah awal."
    )
with kolom_info:
    st.markdown("""
    <div class="info-card">
        <div class="small-note">WAKTU PARUH REFERENSI</div>
        <h2 style="color:#176B87; margin:5px 0;">5.730 tahun</h2>
        <div class="small-note">Waktu yang diperlukan agar jumlah Karbon-14
        berkurang menjadi setengah dari jumlah awal.</div>
    </div>
    """, unsafe_allow_html=True)

# 02 CALCULATION
N = persentase / 100
usia = math.log(N) / k
st.markdown('<div class="section-title">02 / Hasil Simulasi</div>', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
c1.metric("Karbon-14 Tersisa", f"{persentase}%")
c2.metric("Konstanta Peluruhan", f"{k:.8f} tahun⁻¹")
c3.metric("Perkiraan Usia", f"{usia:,.0f} tahun")
st.success(f"Berdasarkan model, perkiraan usia sampel adalah {usia:,.0f} tahun.")

# 03 CARBON-14 GRAPH
st.markdown('<div class="section-title">03 / Visualisasi Peluruhan Karbon-14</div>', unsafe_allow_html=True)
t = np.linspace(0, 6 * waktu_paruh, 400)
jumlah = 100 * np.exp(k * t)
fig, ax = plt.subplots(figsize=(11, 5))
fig.patch.set_facecolor("white")
ax.set_facecolor("#F8FAFC")
ax.plot(t, jumlah, color="#176B87", linewidth=3, label="Kurva peluruhan Karbon-14")
ax.axhline(persentase, color="#E07A5F", linestyle="--", linewidth=2, label=f"Sisa {persentase}%")
ax.axvline(usia, color="#E07A5F", linestyle=":", linewidth=2, label=f"Usia {usia:,.0f} tahun")
ax.scatter([usia], [persentase], color="#E07A5F", s=80, zorder=5)
ax.set_xlabel("Waktu (tahun)")
ax.set_ylabel("Karbon-14 tersisa (%)")
ax.set_title("Peluruhan Radioaktif Karbon-14", fontsize=15, fontweight="bold", pad=15)
ax.set_ylim(0, 105)
ax.set_xlim(0, 6 * waktu_paruh)
ax.grid(True, alpha=0.2)
ax.legend(frameon=False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
st.pyplot(fig, use_container_width=True)
plt.close(fig)
st.caption("Persentase pada slider merupakan input simulasi, bukan data pengukuran sampel nyata.")

# 04 MODEL MATH
st.markdown('<div class="section-title">04 / Model Matematika</div>', unsafe_allow_html=True)
tab1, tab2, tab3 = st.tabs(["Persamaan Diferensial", "Penyelesaian Analitis", "Interpretasi Fisis"])
with tab1:
    st.markdown("**Persamaan diferensial orde satu:**")
    st.latex(r"\frac{dN}{dt}=kN")
    st.markdown("""
    Keterangan:
    - `N(t)` = jumlah relatif Karbon-14 pada waktu `t`
    - `k` = konstanta peluruhan
    - `t` = waktu dalam tahun
    """)
    st.markdown("Konstanta peluruhan ditentukan dari waktu paruh:")
    st.latex(r"k=\frac{\ln(0.5)}{5730}")
    st.latex(r"k\approx -0.00012097\ \text{tahun}^{-1}")
with tab2:
    st.markdown("Pemisahan variabel menghasilkan:")
    st.latex(r"\frac{dN}{N}=k\,dt")
    st.markdown("Integrasikan kedua sisi:")
    st.latex(r"\ln|N|=kt+C")
    st.markdown("Dengan kondisi awal `N(0) = N_0`, diperoleh:")
    st.latex(r"N(t)=N_0e^{kt}")
    st.markdown("Untuk memperkirakan usia sampel:")
    st.latex(r"t=\frac{\ln(N/N_0)}{k}")
with tab3:
    st.markdown("""
    - Nilai `k` negatif menunjukkan jumlah Karbon-14 berkurang.
    - Semakin kecil persentase Karbon-14 yang tersisa, semakin besar perkiraan usia sampel.
    - Model mengasumsikan peluruhan eksponensial sederhana.
    - Penanggalan radiokarbon nyata memerlukan pengukuran sampel dan kalibrasi tambahan.
    """)

# 05 ISOTOPE COMPARISON
st.markdown('<div class="section-title">05 / Perbandingan Laju Peluruhan Antar Isotop</div>', unsafe_allow_html=True)
st.write("Bandingkan persentase zat radioaktif yang tersisa pada beberapa isotop berdasarkan waktu paruh masing-masing.")

isotop = {
    "Karbon-14": 5730.0,
    "Cesium-137": 30.05,
    "Kobalt-60": 5.27
}
pilihan_isotop = st.multiselect(
    "Pilih isotop pada grafik",
    options=list(isotop.keys()),
    default=list(isotop.keys())
)
rentang_tahun = st.slider(
    "Rentang waktu perbandingan (tahun)",
    min_value=10, max_value=30000, value=100, step=10
)

if pilihan_isotop:
    waktu_perbandingan = np.linspace(0, rentang_tahun, 500)
    fig2, ax2 = plt.subplots(figsize=(11, 5))
    fig2.patch.set_facecolor("white")
    ax2.set_facecolor("#F8FAFC")
    for nama in pilihan_isotop:
        T = isotop[nama]
        k_isotop = math.log(0.5) / T
        sisa = 100 * np.exp(k_isotop * waktu_perbandingan)
        ax2.plot(waktu_perbandingan, sisa, linewidth=2.5,
                 label=f"{nama} (waktu paruh {T:g} tahun)")
    ax2.set_xlabel("Waktu (tahun)")
    ax2.set_ylabel("Zat radioaktif tersisa (%)")
    ax2.set_title("Perbandingan Peluruhan Antar Isotop", fontsize=15, fontweight="bold")
    ax2.set_ylim(0, 105)
    ax2.set_xlim(0, rentang_tahun)
    ax2.grid(True, alpha=0.25)
    ax2.legend(frameon=False)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    plt.tight_layout()
    st.pyplot(fig2, use_container_width=True)
    plt.close(fig2)

    st.markdown("**Tabel perbandingan waktu paruh**")
    st.dataframe({
        "Isotop": pilihan_isotop,
        "Waktu paruh (tahun)": [isotop[nama] for nama in pilihan_isotop],
        "Konstanta peluruhan (per tahun)": [
            math.log(0.5) / isotop[nama] for nama in pilihan_isotop
        ]
    }, use_container_width=True, hide_index=True)

    st.info("Semakin pendek waktu paruh suatu isotop, semakin cepat persentase zat radioaktifnya berkurang. Pada rentang waktu yang panjang, isotop dengan waktu paruh pendek dapat tampak mendekati nol.")
else:
    st.warning("Pilih setidaknya satu isotop untuk menampilkan grafik.")

st.caption("Waktu paruh isotop pembanding adalah nilai referensi pendekatan. Grafik merupakan perbandingan model, bukan pengukuran sampel.")

# 06 NOTES AND REFERENCES
st.markdown('<div class="section-title">06 / Catatan dan Sumber</div>', unsafe_allow_html=True)
st.write("Persentase Karbon-14 pada slider merupakan input simulasi, bukan data pengukuran fosil tertentu. Hasil usia merupakan estimasi matematis sederhana.")
st.markdown("**Referensi Karbon-14**")
st.markdown("- [Smithsonian Institution — Radiocarbon Dating](https://humanorigins.si.edu/evidence/dating)")
st.markdown("- [NOAA — Radioactive Decay](https://gml.noaa.gov/outreach/isotopes/decay.html)")
st.markdown("""
<div style="text-align:center; color:#64748B; font-size:12px; padding:15px;">
CARBON-14 DECAY SIMULATOR | PROJECT PEMODELAN MATEMATIKA
</div>
""", unsafe_allow_html=True)
