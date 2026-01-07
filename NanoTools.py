import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go 

# ==========================================
# 1. DATABASE 118 UNSUR & LINK MSDS PUBCHEM
# ==========================================
# Database lengkap untuk mendukung fitur di menu Tools
ELEMENTS = {
    "Hydrogen": {"Sym": "H", "No": 1, "CID": "783"},
    "Helium": {"Sym": "He", "No": 2, "CID": "23987"},
    "Lithium": {"Sym": "Li", "No": 3, "CID": "3028194"},
    "Beryllium": {"Sym": "Be", "No": 4, "CID": "5460467"},
    "Boron": {"Sym": "B", "No": 5, "CID": "5462311"},
    "Carbon": {"Sym": "C", "No": 6, "CID": "5462310"},
    "Nitrogen": {"Sym": "N", "No": 7, "CID": "947"},
    "Oxygen": {"Sym": "O", "No": 8, "CID": "977"},
    "Fluorine": {"Sym": "F", "No": 9, "CID": "24524"},
    "Neon": {"Sym": "Ne", "No": 10, "CID": "23935"},
    "Sodium": {"Sym": "Na", "No": 11, "CID": "5360545"},
    "Magnesium": {"Sym": "Mg", "No": 12, "CID": "5462224"},
    "Aluminum": {"Sym": "Al", "No": 13, "CID": "5359268"},
    "Silicon": {"Sym": "Si", "No": 14, "CID": "5461123"},
    "Phosphorus": {"Sym": "P", "No": 15, "CID": "5462309"},
    "Sulfur": {"Sym": "S", "No": 16, "CID": "5362487"},
    "Chlorine": {"Sym": "Cl", "No": 17, "CID": "24526"},
    "Argon": {"Sym": "Ar", "No": 18, "CID": "23968"},
    "Potassium": {"Sym": "K", "No": 19, "CID": "5462222"},
    "Calcium": {"Sym": "Ca", "No": 20, "CID": "5460341"},
    "Scandium": {"Sym": "Sc", "No": 21, "CID": "5460340"},
    "Titanium": {"Sym": "Ti", "No": 22, "CID": "23963"},
    "Vanadium": {"Sym": "V", "No": 23, "CID": "23990"},
    "Chromium": {"Sym": "Cr", "No": 24, "CID": "23976"},
    "Manganese": {"Sym": "Mn", "No": 25, "CID": "23930"},
    "Iron": {"Sym": "Fe", "No": 26, "CID": "23925"},
    "Cobalt": {"Sym": "Co", "No": 27, "CID": "104730"},
    "Nickel": {"Sym": "Ni", "No": 28, "CID": "935"},
    "Copper": {"Sym": "Cu", "No": 29, "CID": "23978"},
    "Zinc": {"Sym": "Zn", "No": 30, "CID": "23994"},
    "Gallium": {"Sym": "Ga", "No": 31, "CID": "5360835"},
    "Germanium": {"Sym": "Ge", "No": 32, "CID": "5460715"},
    "Arsenic": {"Sym": "As", "No": 33, "CID": "5359596"},
    "Selenium": {"Sym": "Se", "No": 34, "CID": "5360372"},
    "Bromine": {"Sym": "Br", "No": 35, "CID": "24408"},
    "Krypton": {"Sym": "Kr", "No": 36, "CID": "23991"},
    "Rubidium": {"Sym": "Rb", "No": 37, "CID": "5462223"},
    "Strontium": {"Sym": "Sr", "No": 38, "CID": "5460339"},
    "Yttrium": {"Sym": "Y", "No": 39, "CID": "5460338"},
    "Zirconium": {"Sym": "Zr", "No": 40, "CID": "23995"}, 
    "Niobium": {"Sym": "Nb", "No": 41, "CID": "23934"},
    "Molybdenum": {"Sym": "Mo", "No": 42, "CID": "23932"},
    "Technetium": {"Sym": "Tc", "No": 43, "CID": "23959"},
    "Ruthenium": {"Sym": "Ru", "No": 44, "CID": "23955"},
    "Rhodium": {"Sym": "Rh", "No": 45, "CID": "23954"},
    "Palladium": {"Sym": "Pd", "No": 46, "CID": "23938"},
    "Silver": {"Sym": "Ag", "No": 47, "CID": "23954"},
    "Cadmium": {"Sym": "Cd", "No": 48, "CID": "23973"},
    "Indium": {"Sym": "In", "No": 49, "CID": "5360965"},
    "Tin": {"Sym": "Sn", "No": 50, "CID": "5352426"},
    "Antimony": {"Sym": "Sb", "No": 51, "CID": "5354495"},
    "Tellurium": {"Sym": "Te", "No": 52, "CID": "5362488"},
    "Iodine": {"Sym": "I", "No": 53, "CID": "24442"},
    "Xenon": {"Sym": "Xe", "No": 54, "CID": "23993"},
    "Cesium": {"Sym": "Cs", "No": 55, "CID": "5462221"},
    "Barium": {"Sym": "Ba", "No": 56, "CID": "5460337"},
    "Lanthanum": {"Sym": "La", "No": 57, "CID": "5460336"},
    "Cerium": {"Sym": "Ce", "No": 58, "CID": "5460335"},
    "Praseodymium": {"Sym": "Pr", "No": 59, "CID": "5460334"},
    "Neodymium": {"Sym": "Nd", "No": 60, "CID": "5460333"},
    "Promethium": {"Sym": "Pm", "No": 61, "CID": "5460332"},
    "Samarium": {"Sym": "Sm", "No": 62, "CID": "5460331"},
    "Europium": {"Sym": "Eu", "No": 63, "CID": "5460330"},
    "Gadolinium": {"Sym": "Gd", "No": 64, "CID": "5460329"},
    "Terbium": {"Sym": "Tb", "No": 65, "CID": "5460328"},
    "Dysprosium": {"Sym": "Dy", "No": 66, "CID": "5460327"},
    "Holmium": {"Sym": "Ho", "No": 67, "CID": "5460326"},
    "Erbium": {"Sym": "Er", "No": 68, "CID": "5460325"},
    "Thulium": {"Sym": "Tm", "No": 69, "CID": "5460324"},
    "Ytterbium": {"Sym": "Yb", "No": 70, "CID": "5460323"},
    "Lutetium": {"Sym": "Lu", "No": 71, "CID": "5460322"},
    "Hafnium": {"Sym": "Hf", "No": 72, "CID": "23986"},
    "Tantalum": {"Sym": "Ta", "No": 73, "CID": "23958"},
    "Tungsten": {"Sym": "W", "No": 74, "CID": "23966"},
    "Rhenium": {"Sym": "Re", "No": 75, "CID": "23953"},
    "Osmium": {"Sym": "Os", "No": 76, "CID": "23937"},
    "Iridium": {"Sym": "Ir", "No": 77, "CID": "23924"},
    "Platinum": {"Sym": "Pt", "No": 78, "CID": "23939"},
    "Gold": {"Sym": "Au", "No": 79, "CID": "23985"},
    "Mercury": {"Sym": "Hg", "No": 80, "CID": "23931"},
    "Thallium": {"Sym": "Tl", "No": 81, "CID": "5362544"},
    "Lead": {"Sym": "Pb", "No": 82, "CID": "5352425"},
    "Bismuth": {"Sym": "Bi", "No": 83, "CID": "5352424"},
    "Polonium": {"Sym": "Po", "No": 84, "CID": "5460677"},
    "Astatine": {"Sym": "At", "No": 85, "CID": "5460492"},
    "Radon": {"Sym": "Rn", "No": 86, "CID": "23952"},
    "Francium": {"Sym": "Fr", "No": 87, "CID": "5462220"},
    "Radium": {"Sym": "Ra", "No": 88, "CID": "5460331"},
    "Actinium": {"Sym": "Ac", "No": 89, "CID": "5460330"},
    "Thorium": {"Sym": "Th", "No": 90, "CID": "5359306"},
    "Protactinium": {"Sym": "Pa", "No": 91, "CID": "5460424"},
    "Uranium": {"Sym": "U", "No": 92, "CID": "23967"},
    "Neptunium": {"Sym": "Np", "No": 93, "CID": "23936"},
    "Plutonium": {"Sym": "Pu", "No": 94, "CID": "23940"},
    "Americium": {"Sym": "Am", "No": 95, "CID": "23969"},
    "Curium": {"Sym": "Cm", "No": 96, "CID": "23977"},
    "Berkelium": {"Sym": "Bk", "No": 97, "CID": "23970"},
    "Californium": {"Sym": "Cf", "No": 98, "CID": "23974"},
    "Einsteinium": {"Sym": "Es", "No": 99, "CID": "23979"},
    "Fermium": {"Sym": "Fm", "No": 100, "CID": "23980"},
    "Mendelevium": {"Sym": "Md", "No": 101, "CID": "23933"},
    "Nobelium": {"Sym": "No", "No": 102, "CID": "23992"},
    "Lawrencium": {"Sym": "Lr", "No": 103, "CID": "23926"},
    "Rutherfordium": {"Sym": "Rf", "No": 104, "CID": "23956"},
    "Dubnium": {"Sym": "Db", "No": 105, "CID": "23921"},
    "Seaborgium": {"Sym": "Sg", "No": 106, "CID": "23957"},
    "Bohrium": {"Sym": "Bh", "No": 107, "CID": "23971"},
    "Hassium": {"Sym": "Hs", "No": 108, "CID": "23988"},
    "Meitnerium": {"Sym": "Mt", "No": 109, "CID": "23929"},
    "Darmstadtium": {"Sym": "Ds", "No": 110, "CID": "23920"},
    "Roentgenium": {"Sym": "Rg", "No": 111, "CID": "23951"},
    "Copernicium": {"Sym": "Cn", "No": 112, "CID": "23927"},
    "Nihonium": {"Sym": "Nh", "No": 113, "CID": "135246755"},
    "Flerovium": {"Sym": "Fl", "No": 114, "CID": "135246756"},
    "Moscovium": {"Sym": "Mc", "No": 115, "CID": "135246757"},
    "Livermorium": {"Sym": "Lv", "No": 116, "CID": "135246758"},
    "Tennessine": {"Sym": "Ts", "No": 117, "CID": "135246759"},
    "Oganesson": {"Sym": "Og", "No": 118, "CID": "135246760"},
}

# ==========================================
# 1. KONFIGURASI HALAMAN
# ==========================================
st.set_page_config(page_title="NanoTools", page_icon="🌀", layout="centered")

# =============================
# 2. CUSTOM CSS (TEMA BIRU)
# =============================
st.markdown(f"""
<style>
    /* Latar Belakang Utama Biru #547792 */
    .stApp {{
        background-color: #547792;
    }}
    
    /* Header Utama Biru Gelap #213448 */
    .main-header {{
        background-color: #213448;
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        border-bottom: 4px solid #94B4C1;
    }}

    /* Sidebar Styling */
    [data-testid="stSidebar"] {{
        background-color: #213448;
    }}
    [data-testid="stSidebar"] * {{
        color: white !important;
    }}

    /* Kartu Konten Putih agar Teks Terbaca */
    .card {{
        background-color: rgba(255, 255, 255, 0.95);
        padding: 20px;
        border-radius: 15px;
        color: #213448;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        margin-bottom: 20px;
    }}

    /* Tombol */
    .stButton>button {{
        background-color: #213448;
        color: white;
        width: 100%;
        border-radius: 8px;
        border: 1px solid #94B4C1;
    }}
    
    /* Warna Tab */
    .stTabs [data-baseweb="tab"] {{
        color: white; 
    }}
</style>
""", unsafe_allow_html=True)

# =============================
# 3. SIDEBAR & NAVIGASI
# =============================
with st.sidebar:
    st.title("Menu Utama")
    menu = st.radio("Pilih Modul:", ["📈 Insight", "🔬 Lab Nanoteknologi", "🛠 Tools", "👥 About"])

# =============================
# 4. LOGIKA HALAMAN UTAMA
# =============================
st.markdown("<h1 style='text-align:center; color:white;'>🧬 NanoTools</h1>", unsafe_allow_html=True)

if menu == "📈 Insight":
    st.markdown("<div class='main-header'><h2>📈 Nanotechnology Insights</h2></div>", unsafe_allow_html=True)

    # --- BAGIAN 1: DEFINISI & SKALA ---
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("APA ITU NANOMATERIAL?")
    url = "gifnanomaterial.gif"
    st.image(url, caption="Skema Nanomaterial", use_container_width=True)
    st.write("""
    **Nanomaterial** adalah material yang memiliki ukuran sangat kecil, yaitu pada skala nanometer (sekitar 1–100 nm), sehingga menunjukkan sifat fisik, kimia, dan biologis yang berbeda dibandingkan material berukuran biasa. Karena ukurannya yang sangat kecil, nanomaterial sering memiliki reaktivitas tinggi, luas permukaan besar, dan kinerja yang lebih baik, sehingga banyak dimanfaatkan dalam bidang kesehatan, pangan, energi, dan teknologi.

    """)

    # Membuat 4 kolom dalam 1 baris
    col1, col2, col3, col4 = st.columns(4)

    # NANOMATERIAL 0D
    with col1:
        st.image("1d.jpeg", use_container_width=True)
        st.markdown("<p style='text-align: center; font-weight: bold; margin-bottom: 0;'>Nanopartikel 0D</p>", unsafe_allow_html=True)
        st.markdown("<center><span class='role-badge' style='font-size: 0.6rem;'>0D (Nol Dimensi): Nanopartikel Seluruh dimensinya (panjang, lebar, dan tinggi) berada dalam skala nano (1–100 nm). Material ini berbentuk seperti titik atau bola-bola sangat kecil. Contoh: Quantum dots, nanopartikel emas (AuNP).</span></center>", unsafe_allow_html=True)

    # NANOMATERIAL 1D
    with col2:
        st.image("2d.jpeg", use_container_width=True)
        st.markdown("<p style='text-align: center; font-weight: bold; margin-bottom: 0;'>Nanopartikel 1D</p>", unsafe_allow_html=True)
        st.markdown("<center><span class='role-badge' style='font-size: 0.6rem;'>1D (Satu Dimensi): Nanowires / Nanotubes Dua dimensi berada dalam skala nano, sedangkan satu dimensi lainnya memanjang (makroskopis). Bentuknya menyerupai jarum, kabel, atau tabung panjang. Contoh: Carbon Nanotubes (CNT), nanowires logam.</span></center>", unsafe_allow_html=True)

    # NANOMATERIAL 2D
    with col3:
        st.image("3d.jpeg", use_container_width=True)
        st.markdown("<p style='text-align: center; font-weight: bold; margin-bottom: 0;'>Nanopartikel 2D</p>", unsafe_allow_html=True)
        st.markdown("<center><span class='role-badge' style='font-size: 0.6rem;'>2D (Dua Dimensi): Nanosheets Hanya satu dimensi (ketebalan) yang berada dalam skala nano, sementara dua dimensi lainnya (luas) berukuran besar. Berbentuk seperti lembaran atau lapisan yang sangat tipis. Contoh: Graphene, nanoclays.</span></center>", unsafe_allow_html=True)

    # NANOMATERIAL 3D
    with col4:
        st.image("4d.jpeg", use_container_width=True)
        st.markdown("<p style='text-align: center; font-weight: bold; margin-bottom: 0;'>Nanopartikel 3D</p>", unsafe_allow_html=True)
        st.markdown("<center><span class='role-badge' style='font-size: 0.6rem;'>3D (Tiga Dimensi): Nanokomposit Secara fisik ukurannya besar (di luar skala nano), namun struktur internalnya tersusun dari material skala nano atau merupakan gabungan dari unit-unit nano yang terdispersi dalam suatu matriks. Contoh: Serat karbon, material polimer yang diperkuat nanopartikel.</span></center>", unsafe_allow_html=True)

    # --- BAGIAN 3: SIFAT UNIK (EFEK UKURAN) ---
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("✨ Mengapa Material Nano Berbeda?")
    
    tab_a, tab_b = st.tabs(["Rasio Permukaan", "Efek Kuantum"])
    
    with tab_a:
        st.write("**Efek Luas Permukaan:** Semakin kecil partikel, semakin banyak atom yang berada di permukaan, membuatnya sangat reaktif.")
        # Grafik simulasi rasio permukaan vs ukuran
        x_size = np.linspace(10, 500, 50)
        y_surface = 6 / x_size # Rumus sederhana rasio S/V kubus
        
        fig_surf = go.Figure()
        fig_surf.add_trace(go.Scatter(x=x_size, y=y_surface, mode='lines', line=dict(color='#213448', width=3)))
        fig_surf.update_layout(title="Rasio Permukaan vs Ukuran Partikel", xaxis_title="Ukuran (nm)", yaxis_title="Rasio S/V")
        st.plotly_chart(fig_surf, use_container_width=True)

    with tab_b:
        st.write("**Efek Kuantum:** Pada skala nano, sifat optik dan elektronik berubah. Contoh: Emas nano bisa berwarna merah atau ungu, bukan kuning.")
        st.info("💡 Ini terjadi karena pembatasan gerak elektron (Quantum Confinement).")
    st.markdown("</div>", unsafe_allow_html=True)

    # --- BAGIAN 4: PERBANDINGAN BULK VS NANO ---
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("⚖️ Perbandingan: Bulk vs Nano")
    comparison = {
        "Properti": ["Warna", "Kereaktifan", "Kekuatan", "Titik Lebur"],
        "Material Bulk": ["Tetap/Konstan", "Rendah", "Standar", "Tinggi"],
        "Material Nano": ["Bergantung Ukuran", "Sangat Tinggi", "Sangat Kuat", "Lebih Rendah"]
    }
    st.table(pd.DataFrame(comparison))
    st.markdown("</div>", unsafe_allow_html=True)

elif menu == "🔬 Lab Nanoteknologi":
    st.subheader("🧪 Kalkulator Lab — Konversi & Persiapan Larutan")
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("Modul ini berisi: konversi satuan (M, mM, µM, N, ppm, ppb), kalkulator pengenceran (C1V1=C2V2), dan kalkulator pembuatan larutan (dari Mr).")

    # ------------------
    # 1) KONVERSI SATUAN
    # ------------------
    st.markdown("### 🔁 Konversi Satuan")
    with st.expander("Buka Konversi Satuan"):
        conv_col1, conv_col2 = st.columns(2)
        with conv_col1:
            conv_from = st.selectbox("Dari:", ["M (mol/L)", "mM (mmol/L)", "µM (µmol/L)", "N (normal)", "ppm (mg/L)", "ppb (µg/L)"])
            val_from = st.number_input("Nilai", value=1.0, format="%.6f")
            mr_conv = st.number_input("Mr (g/mol) — diperlukan kalau konversi melibatkan massa/ppm", min_value=0.0, value=18.015, step=0.1)
        with conv_col2:
            conv_to = st.selectbox("Ke:", ["M (mol/L)", "mM (mmol/L)", "µM (µmol/L)", "N (normal)", "ppm (mg/L)", "ppb (µg/L)"])
            eq_per_mol = st.number_input("Bilangan ekuivalen per mol (untuk Normalitas) — gunakan 1 jika tidak tahu", min_value=0.0, value=1.0, step=1.0)

        def convert_units(value, frm, to, mr, eq):
            # Normalisasi semua ke molarity (mol/L) sebagai basis bila memungkinkan
            # Konversi masuk -> mol/L
            if frm == "M (mol/L)":
                mol_L = value
            elif frm == "mM (mmol/L)":
                mol_L = value / 1000.0
            elif frm == "µM (µmol/L)":
                mol_L = value / 1e6
            elif frm == "N (normal)":
                # N = equiv/L ; mol/L = N / eq_per_mol
                if eq == 0:
                    mol_L = 0
                else:
                    mol_L = value / eq
            elif frm == "ppm (mg/L)":
                # asumsi: larutan berair, 1 ppm = 1 mg/L; mg/L -> g/L -> mol/L
                mol_L = (value / 1000.0) / mr if mr > 0 else 0
            elif frm == "ppb (µg/L)":
                mol_L = (value / 1e6) / mr if mr > 0 else 0
            else:
                mol_L = 0

            # Konversi mol/L -> tujuan
            if to == "M (mol/L)":
                return mol_L
            elif to == "mM (mmol/L)":
                return mol_L * 1000.0
            elif to == "µM (µmol/L)":
                return mol_L * 1e6
            elif to == "N (normal)":
                return mol_L * eq
            elif to == "ppm (mg/L)":
                # mol/L -> g/L -> mg/L
                return mol_L * mr * 1000.0
            elif to == "ppb (µg/L)":
                return mol_L * mr * 1e6
            else:
                return None

        if st.button("Konversi", key="konv"):
            try:
                result = convert_units(val_from, conv_from, conv_to, mr_conv, eq_per_mol)
                st.success(f"Hasil: {result:.6g} {conv_to}")
                # Tampilkan juga penjelasan singkat
                st.caption("Catatan: untuk konversi ppm/ppb kami mengasumsikan kerapatan larutan = 1 g/mL (air). Normalitas memerlukan bilangan ekuivalen per mol.")
            except Exception as e:
                st.error(f"Gagal mengonversi: {e}")

    st.markdown("---")

    # ------------------
    # 2) KALKULATOR PENGENCERAN (C1V1 = C2V2)
    # ------------------
    st.markdown("### 🔬 Kalkulator Pengenceran (C1V1 = C2V2)")
    with st.expander("Buka Kalkulator Pengenceran"):
        dc1, dc2 = st.columns(2)
        with dc1:
            c1 = st.number_input("C1 (konsentrasi stok)", value=1.0, format="%.6g")
            u1 = st.selectbox("Unit C1", ["M", "mM", "µM", "% (w/v)", "g/L"], key="u1")
            v2 = st.number_input("V2 (volume akhir yang diinginkan)", value=100.0, format="%.6g")
            u_v2 = st.selectbox("Unit Volume V2", ["mL", "L"], index=0, key="uv2")
        with dc2:
            c2 = st.number_input("C2 (konsentrasi akhir yang diinginkan)", value=0.1, format="%.6g")
            u2 = st.selectbox("Unit C2", ["M", "mM", "µM", "% (w/v)", "g/L"], key="u2")
            v1 = st.number_input("V1 (volume stok yg diperlukan) — kosongkan 0 untuk dihitung", value=0.0, format="%.6g")
            u_v1 = st.selectbox("Unit Volume V1", ["mL", "L"], index=0, key="uv1")

        # Helper untuk normalisasi konsentrasi ke mol/L bila unit M/mM/µM, atau ke g/L jika % atau g/L
        def normalize_conc_to_molL(c, unit, mr=0):
            if unit == "M":
                return c
            elif unit == "mM":
                return c / 1000.0
            elif unit == "µM":
                return c / 1e6
            elif unit == "% (w/v)":
                # % w/v = g per 100 mL -> g/L = % * 10 ; mol/L = g/L / Mr
                g_per_L = c * 10.0
                return (g_per_L / mr) if mr > 0 else None
            elif unit == "g/L":
                return (c / mr) if mr > 0 else None
            else:
                return None

        if st.button("Hitung V1 (atau C1 jika V1=0)", key="dilute"):
            try:
                # convert volumes to L
                V2_L = v2 / 1000.0 if u_v2 == "mL" else v2
                # Try compute V1 if C1 known
                C1_mol = normalize_conc_to_molL(c1, u1, mr_conv)
                C2_mol = normalize_conc_to_molL(c2, u2, mr_conv)
                if C1_mol is None or C2_mol is None:
                    st.error("Tidak bisa menghitung: pastikan Mr diisi jika menggunakan unit % atau g/L.")
                else:
                    V1_L = (C2_mol * V2_L) / C1_mol
                    V1 = V1_L * 1000.0 if u_v1 == "mL" else V1_L
                    st.success(f"Volume stok yang diperlukan V1 = {V1:.6g} {u_v1}")
                    st.caption("Rumus yang digunakan: C1*V1 = C2*V2 (unit konsentrasi harus sebanding, maka kami konversi ke mol/L)")
            except Exception as e:
                st.error(f"Gagal menghitung pengenceran: {e}")

    st.markdown("---")

    # ------------------
    # 3) KALKULATOR PEMBUATAN LARUTAN (GRAM YG HARUS DITIMBANG)
    # ------------------
    st.markdown("### ⚖️ Kalkulator Pembuatan Larutan (Hitung gram padatan)")
    with st.expander("Buka Kalkulator Pembuatan Larutan"):
        colp1, colp2 = st.columns(2)
        with colp1:
            mr_input = st.number_input("Mr (g/mol)", min_value=0.0, value=mr_conv, step=0.01)
            desired_conc = st.number_input("Konsentrasi yang diinginkan (angka saja)", min_value=0.0, value=0.1, step=0.0001, format="%.6g")
            conc_unit = st.selectbox("Unit konsentrasi:", ["M","mM","µM","g/L","% (w/v)"])
        with colp2:
            vol_val = st.number_input("Volume yang ingin dibuat", min_value=0.0, value=100.0, step=0.1)
            vol_unit = st.selectbox("Unit volume:", ["mL","L"], index=0)

        def grams_needed(mr, conc, conc_unit, vol, vol_unit):
            # convert volume to L
            V_L = vol / 1000.0 if vol_unit == "mL" else vol
            if conc_unit == "M":
                # gram = M (mol/L) * Mr (g/mol) * V (L)
                return conc * mr * V_L
            elif conc_unit == "mM":
                return (conc / 1000.0) * mr * V_L
            elif conc_unit == "µM":
                return (conc / 1e6) * mr * V_L
            elif conc_unit == "g/L":
                return conc * V_L
            elif conc_unit == "% (w/v)":
                # % w/v = g/100mL; grams = % * (vol_mL / 100)
                vol_mL = vol if vol_unit == "mL" else vol * 1000.0
                return conc * (vol_mL / 100.0)
            else:
                return None

        if st.button("Hitung Gram yang Harus Ditimbang", key="prep"):
            try:
                grams = grams_needed(mr_input, desired_conc, conc_unit, vol_val, vol_unit)
                if grams is None:
                    st.error("Unit tidak dikenali")
                else:
                    st.success(f"Timbang sebanyak: {grams:.6g} gram")
                    st.caption("Catatan: cek kemurnian reagen dan sesuaikan massa aktual jika reagen tidak murni.")
            except Exception as e:
                st.error(f"Gagal menghitung: {e}")

    st.markdown("</div>", unsafe_allow_html=True)

elif menu == "🛠 Tools":
    st.subheader("🛠 Integrated Safety Tools")
    # Existing Tools content (kept as in original file)...
    tab1, tab2, tab3= st.tabs(["Tabel MSDS 118 Unsur", "Sifat Nanomaterial"])
    
    with tab1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 🛡️ Database Keselamatan Elemen")
        st.write("Cari informasi keselamatan resmi dari PubChem.")
        pilihan = st.selectbox("Cari Unsur (Bahasa Inggris):", list(ELEMENTS.keys()))
        if pilihan:
            data = ELEMENTS[pilihan]
            msds_url = f"https://pubchem.ncbi.nlm.nih.gov/compound/{data['CID']}#section=Safety-and-Hazards"
            st.markdown(f"#### 📊 Identitas Kimia: {pilihan}")
            df_info = pd.DataFrame({
                "Parameter": ["Simbol", "Nomor Atom", "PubChem CID"],
                "Detail": [data["Sym"], data["No"], data["CID"]]
            })
            st.table(df_info)
            st.warning(f"⚠️ Periksa Bahaya GHS untuk {pilihan}")
            st.markdown(f'''<a href="{msds_url}" target="_blank">
                <button style="width:100%; border-radius:10px; padding:10px; background-color:#DE1A58; color:white; border:none; cursor:pointer; font-weight:bold;">
                KLIK UNTUK MSDS LENGKAP {pilihan.upper()}
                </button></a>''', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### Nano-Converter")
        st.write("Analisis perubahan sifat fisik dan kimia atom pada skala nanometer.")
        pilihan_nano = st.selectbox("Pilih Unsur untuk Konversi Nano:", list(ELEMENTS.keys()))
        size_nano = st.slider("Atur Ukuran Partikel (nm):", 1, 1000, 1000, key="slider_nano")
        if size_nano <= 100:
            st.error(f"✨ *MODE NANO AKTIF: {pilihan_nano}*")
            ratio_nano = 6 / size_nano 
            st.metric(label="Rasio Luas Permukaan : Volume", value=f"{ratio_nano:.2f}")
            def get_nano_properties(element):
                if element in ["Silver", "Gold", "Platinum"]:
                    return {"Hambat": "Sangat Tinggi (Interaksi ion permukaan dengan membran sel).",
                            "Warna": "Berubah drastis (Efek LSPR - Surface Plasmon Resonance).",
                            "Larut": "Dispersi koloid stabil, meningkatkan efektivitas dalam cairan."}
                elif element in ["Iron", "Zinc", "Copper", "Magnesium", "Calcium"]:
                    return {"Hambat": "Moderat (Memicu ROS/Stres Oksidatif pada bakteri).",
                            "Warna": "Lebih gelap/intens karena luas permukaan yang besar.",
                            "Larut": "Bioavailabilitas meningkat drastis (Sangat mudah diserap tubuh)."}
                elif element in ["Silicon", "Carbon", "Selenium"]:
                    return {"Hambat": "Spesifik (Bergantung pada modifikasi permukaan/fungsionalisasi).",
                            "Warna": "Cenderung transparan atau hitam (bergantung pada struktur nano).",
                            "Larut": "Daya ikat (adsorpsi) meningkat drastis."}
                else:
                    return {"Hambat": "Bergantung pada reaktivitas atom di permukaan.",
                            "Warna": "Pergeseran spektrum cahaya akibat ukuran partikel.",
                            "Larut": "Peningkatan kinetika pelarutan karena rasio luas permukaan."}
            sifat = get_nano_properties(pilihan_nano)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.info(f" *Daya Hambat*\n\n{sifat['Hambat']}")
            with col2:
                st.warning(f" *Warna*\n\n{sifat['Warna']}")
            with col3:
                st.success(f" *Kelarutan*\n\n{sifat['Larut']}")
        else:
            st.info("📦 *Sifat Makro (Bulk):* Material masih berukuran besar. Geser slider di bawah 100 nm untuk melihat sifat spesifik nanometer.")
        st.markdown("</div>", unsafe_allow_html=True)
        

elif menu == "👥 About":
    st.markdown("## 👥 Tim Pengembang NanoTools")
    st.markdown("<div class='card-header'>Tentang NanoTools</div>", unsafe_allow_html=True)
    st.write("""
    Website ini dikembangkan oleh mahasiswa prodi Nanoteknologi Pangan untuk mendigitalisasi 
    perhitungan laboratorium dan mempermudah akses literatur nanoteknologi.
    """)
    
    st.markdown("### 🚀 Fitur Utama")
    st.markdown("""
    * **Simulasi Sintesis Nanopartikel**: *Visualisasi skema metode **Bottom-Up** dan **Top-Down** untuk membantu pemahaman mekanisme pembentukan partikel skala nano.*
    * **Analisis Karakterisasi Digital**: *Modul bantu untuk mengolah data awal hasil karakterisasi laboratorium dengan standar komputasi yang akurat.*
    * **Database Material Nano**: *Akses cepat ke referensi properti material nanomaterial pangan dan umum untuk mendukung studi literatur.*
    * **Database MSDS**: *Penyediaan lembar data keselamatan bahan kimia (MSDS) untuk memastikan prosedur penanganan bahan di laboratorium dilakukan dengan aman dan sesuai standar K3.*
    """)

    st.markdown("### Anggota Tim")
    st.write("") # Spacer

    # Membuat 4 kolom dalam 1 baris
    col1, col2, col3, col4 = st.columns(4)

    # PENULIS 1
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/4140/4140048.png", use_container_width=True)
        st.markdown("<p style='text-align: center; font-weight: bold; margin-bottom: 0;'>Fairuz Zuhria Chayara Alima</p>", unsafe_allow_html=True)
        st.markdown("<center><span class='role-badge' style='font-size: 0.6rem;'>Penulis</span></center>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size: 0.7rem; color: #666;'>NIM: 2450156</p>", unsafe_allow_html=True)

    # PENULIS 2
    with col2:
        st.image("fotointann.jpeg", use_container_width=True)
        st.markdown("<p style='text-align: center; font-weight: bold; margin-bottom: 0;'>Intan Nurul Hasanah</p>", unsafe_allow_html=True)
        st.markdown("<center><span class='role-badge' style='font-size: 0.6rem;'>Penulis</span></center>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size: 0.7rem; color: #666;'>NIM: 2450167</p>", unsafe_allow_html=True)

    # PENULIS 3
    with col3:
        st.image("foto gue.jpeg", use_container_width=True)
        st.markdown("<p style='text-align: center; font-weight: bold; margin-bottom: 0;'>Meuthia Zulashfi Rhohyan Syafrudin</p>", unsafe_allow_html=True)
        st.markdown("<center><span class='role-badge' style='font-size: 0.6rem;'>Penulis</span></center>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size: 0.7rem; color: #666;'>NIM: 2450180</p>", unsafe_allow_html=True)

    # PENULIS 4
    with col4:
        st.image("fotoniko.jpeg", use_container_width=True)
        st.markdown("<p style='text-align: center; font-weight: bold; margin-bottom: 0;'>Nicholas Dimas Ananda</p>", unsafe_allow_html=True)
        st.markdown("<center><span class='role-badge' style='font-size: 0.6rem;'>Penulis</span></center>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size: 0.7rem; color: #666;'>NIM: 2450197</p>", unsafe_allow_html=True)


    # --- Info Instansi ---
    st.markdown("---")
    st.markdown("<h4 style='text-align: center; color: white;'>Politeknik AKA Bogor</h4>", unsafe_allow_html=True)


# =============================
# FOOTER
# =============================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white; font-size: 0.8rem;'>Hak Cipta © 2025 NanoTools. All Rights Reserved.</p>", unsafe_allow_html=True)
