import streamlit as st
import pandas as pd
import numpy as np

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

# =============================
# 2. KONFIGURASI HALAMAN & CSS
# =============================
st.set_page_config(page_title="NanoTools Pro", page_icon="🧬", layout="centered")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(-45deg, #360185, #8F0177, #DE1A58, #F4B342);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
}
@keyframes gradient {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
.card {
    background: rgba(255, 255, 255, 0.9);
    padding: 20px;
    border-radius: 15px;
    color: #333;
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
}
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
st.markdown("<h1 style='text-align:center; color:white;'>🧬 NanoTools Pro</h1>", unsafe_allow_html=True)

if menu == "📈 Insight":
    st.subheader("📊 Research Insight")
    st.line_chart(pd.DataFrame(np.random.randn(20, 2), columns=['Nano-A', 'Nano-B']))

elif menu == "🔬 Lab Nanoteknologi":
    st.subheader("🧪 Kalkulator Molaritas")
    # Logika untuk menghitung massa (gram) berdasarkan input pengguna
    m = st.number_input("Molaritas (M)", min_value=0.0, step=0.01)
    v = st.number_input("Volume (L)", min_value=0.0, step=0.01)
    mr = st.number_input("Berat Molekul (Mr)", min_value=0.0, step=0.1)
    if st.button("Hitung"):
        st.success(f"Hasil: {m*v*mr:.4f} gram")

elif menu == "🛠 Tools":
    st.subheader("🛠 Integrated Safety Tools")
    # Menggabungkan database unsur lokal ke dalam tab menu Tools
    tab1, tab2 = st.tabs(["🧬 Tabel MSDS 118 Unsur", "🍽️ Food Tools"])
    
    with tab1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 🛡️ Database Keselamatan Elemen")
        st.write("Cari informasi keselamatan resmi dari PubChem.")
        
        # Pilihan unsur untuk menampilkan info kimia dan link MSDS
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
        st.write("Simulasi perubahan sifat atom saat dikonversi ke skala nanometer.")

        # Pilihan Material Berbasis Pangan
        material = st.selectbox("Pilih Material:", ["Silver (Ag)", "Gold (Au)", "Iron (Fe)", "Silika (SiO2)"])

        # Slider Skala Nanometer
        st.write("---")
        size = st.slider("Ukuran Partikel (nm):", min_value=1, max_value=1000, value=1000)

        # Logika Perubahan Sifat Atom
        st.write(f"#### Hasil Analisis pada {size} nm:")
        
        if size > 100:
            st.info("📦 **Sifat Makro:** Material bertindak sebagai material curah (bulk). Reaktivitas rendah.")
        else:
            st.error("✨ **Sifat Nano Aktif:**")
            # Rasio luas permukaan (Surface-to-Volume Ratio) meningkat drastis
            # Rumus sederhana: $6/D$ (untuk bola)
            ratio = 6 / size 
            st.metric(label="Rasio Luas Permukaan : Volume", value=f"{ratio:.2f}")
            
            if material == "Silver (Ag)":
                st.write("**Efek:** Daya hambat bakteri (antibakteri) meningkat drastis karena luas permukaan kontak dengan dinding sel mikroba lebih besar.")
            elif material == "Gold (Au)":
                st.write("**Efek:** Warna berubah dari keemasan menjadi merah/ungu karena efek *Localized Surface Plasmon Resonance* (LSPR).")
            elif material == "Iron (Fe)":
                st.write("**Efek:** Kelarutan dan bioavailabilitas dalam tubuh meningkat, sangat efektif untuk fortifikasi pangan.")
            elif material == "Silika (SiO2)":
                st.write("**Efek:** Luas permukaan yang besar membuatnya sangat efektif sebagai zat anti-kempal (anti-caking agent).")

        st.markdown("</div>", unsafe_allow_html=True)

elif menu == "👥 About":
    # Bagian About untuk informasi penulis dan institusi
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("👥 Tentang Aplikasi")
    st.write("**NanoTools Pro** adalah aplikasi asisten laboratorium digital yang dirancang untuk memudahkan peneliti dan mahasiswa dalam kalkulasi kimia serta akses cepat terhadap keamanan bahan kimia (MSDS).")
    
    st.markdown("---")
    st.write("**Penulis:**")
    st.write("👤 **Meutia Zulasfi**")
    st.write("🆔 **NIM: 2420448**")
    
    st.markdown("---")
    st.write("**Institusi:**")
    st.info("Politeknik AKA Bogor - Program Studi Nanoteknologi Pangan")
    st.markdown("</div>", unsafe_allow_html=True)

# Footer aplikasi
st.markdown("<p style='text-align:center; color:white; font-size:0.8rem; margin-top:50px;'>Hak Cipta © 2026 NanoTools Project | Meutia Zulasfi (2420448)</p>", unsafe_allow_html=True)