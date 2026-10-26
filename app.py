
import streamlit as st

st.set_page_config(page_title="EduGuide AI")


st.markdown("""
<style>
.stApp {
    background-color: #f7f7f7;
    color: #262730;
}
.block-container {
    max-width: 760px;
    padding-top: 55px;
}
h1, h2, h3, p, label, .stMarkdown, .stText {
    color: #262730 !important;
}
.job {
    background: white;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 15px;
    box-shadow: 0 2px 8px #dddddd;
}
.job h3 {
    color: #527a96 !important;
}
</style>
""", unsafe_allow_html=True)


st.title("🎓 EduGuide AI")
st.write("Type your interests or courses, and the app will recommend jobs for you!")

interest = st.text_input("Your interests or courses")

jobs = [
("Web Developer", "coding website html web design", "Computer Science, Web Development"),
("Software Developer", "coding software programming apps", "Computer Science, Programming"),
("Game Developer", "gaming games coding video games", "Game Design, Programming"),
("AI Engineer", "artificial intelligence ai robots coding", "AI, Computer Science"),
("Data Scientist", "data statistics analysis patterns", "Data Science, Statistics"),
("Cybersecurity Analyst", "cybersecurity hacking security computers", "Cybersecurity, IT"),
("App Developer", "mobile apps coding android", "App Development, Programming"),
("Robotics Engineer", "robots robotics machines automation", "Robotics, Engineering"),
("Doctor", "medicine biology patients healthcare", "Medical Science, Biology"),
("Surgeon", "surgery medicine operation healthcare", "Medicine, Surgery"),
("Psychiatrist", "mental health psychiatry brain medicine", "MBBS, Psychiatry"),
("Psychologist", "psychology emotions behaviour mind people", "Psychology"),
("Nurse", "nursing patient care hospital", "Nursing, Healthcare"),
("Pharmacist", "medicines drugs pharmacy chemistry", "Pharmacy"),
("Dentist", "teeth dental oral health", "Dental Science"),
("Physiotherapist", "physiotherapy muscles rehabilitation sports injury", "Physiotherapy"),
("Geneticist", "genes genetics dna biology research", "Genetics, Biology"),
("Microbiologist", "microbes bacteria microorganisms laboratory", "Microbiology"),
("Biotechnologist", "biotechnology biology genetics research", "Biotechnology"),
("Veterinarian", "animals pets animal doctor veterinary", "Veterinary Science"),
("Public Speaker", "public speaking speech stage audience", "Communication, Public Speaking"),
("News Anchor", "news anchoring speaking journalism television", "Journalism, Mass Communication"),
("Journalist", "journalism writing reporting news", "Journalism, Media"),
("Lawyer", "law justice debate arguments court", "Law, Legal Studies"),
("Diplomat", "international relations countries diplomacy languages", "International Relations"),
("Teacher", "teaching explaining students education", "Education, Subject Specialisation"),
("English Teacher", "english grammar literature language teaching", "English, Education"),
("Professor", "professor university teaching research academics", "Master's Degree, PhD"),
("School Counsellor", "counselling students guidance emotions", "Psychology, Counselling"),
("Writer", "writing stories books novels literature", "Literature, Creative Writing"),
("Poet", "poetry poems creative writing literature", "Literature, Creative Writing"),
("Translator", "languages translation interpreting communication", "Languages, Translation"),
("Graphic Designer", "graphic design drawing creativity posters", "Graphic Design"),
("Painter", "painting art colours canvas", "Fine Arts"),
("Illustrator", "illustration drawing sketching books", "Illustration, Fine Arts"),
("Fashion Designer", "fashion clothes clothing design textiles", "Fashion Design"),
("Interior Designer", "interior rooms furniture decoration", "Interior Design"),
("Architect", "architecture buildings drawing designing structures", "Architecture"),
("Animator", "animation cartoons characters drawing", "Animation, Digital Arts"),
("Photographer", "photography camera photos pictures", "Photography"),
("Content Creator", "content creation social media videos", "Media, Content Creation"),
("Video Editor", "video editing filmmaking reels youtube", "Video Editing"),
("Actor", "acting theatre drama films performance", "Acting, Theatre Arts"),
("Singer", "singing music vocals songs", "Music, Vocal Training"),
("Musician", "music instruments composing playing", "Music"),
("Dancer", "dancing choreography dance performance", "Dance, Performing Arts"),
("Film Director", "film directing cinema storytelling movies", "Film Studies"),
("Social Media Manager", "social media marketing instagram online", "Digital Marketing"),
("Athlete", "sports athletics competition physical performance", "Sports Science, Training"),
("Footballer", "football soccer sports team", "Sports Training"),
("Cricketer", "cricket batting bowling sports", "Sports Training"),
("Sports Coach", "coaching sports training athletes", "Sports Science"),
("Sports Psychologist", "sports psychology athletes mental performance", "Psychology, Sports Science"),
("Astronaut", "space astronaut planets space travel", "Aerospace, Science"),
("Astronomer", "astronomy stars planets galaxies universe", "Astronomy, Physics"),
("Astrophysicist", "astrophysics stars universe physics space", "Physics, Astrophysics"),
("Aerospace Engineer", "aerospace aircraft spacecraft rockets", "Aerospace Engineering"),
("Aeronautical Engineer", "aeronautics aircraft airplanes flight design", "Aeronautical Engineering"),
("Rocket Engineer", "rockets propulsion spacecraft launch", "Aerospace Engineering"),
("Satellite Engineer", "satellites space communication orbit", "Electronics, Aerospace Engineering"),
("Commercial Pilot", "pilot flying airplanes aviation", "Flight Training"),
("Physicist", "physics matter energy forces experiments", "Physics, Research"),
("Chemist", "chemistry chemicals reactions laboratory", "Chemistry"),
("Research Scientist", "research innovation experiments discovery invention", "Science, Research"),
("Inventor", "inventing invention innovative ideas creating", "Engineering, Design"),
("Environmental Scientist", "environment climate pollution conservation", "Environmental Science"),
("Marine Biologist", "ocean marine animals sea biology", "Marine Biology"),
("Archaeologist", "archaeology ancient history artefacts excavation", "Archaeology, History"),
("Forensic Scientist", "forensics crime investigation evidence laboratory", "Forensic Science"),
("Economist", "economics economy markets society", "Economics"),
("Entrepreneur", "business startup entrepreneurship ideas leadership", "Business Management"),
("Accountant", "accounting accounts finance numbers", "Accounting, Finance"),
("Financial Analyst", "finance investments markets money", "Finance, Economics"),
("Civil Servant", "government administration public service policy", "Civil Services"),
("Police Officer", "police law enforcement investigation", "Police Training, Law"),
("Social Worker", "social work helping communities people", "Social Work"),
("Chef", "cooking food recipes kitchen", "Culinary Arts"),
("Travel Consultant", "travel tourism holidays destinations", "Tourism, Hospitality"),
("Civil Engineer", "construction bridges roads buildings", "Civil Engineering"),
("Mechanical Engineer", "machines mechanical engines manufacturing", "Mechanical Engineering"),
("Electrical Engineer", "electricity circuits electrical systems", "Electrical Engineering"),
("Chemical Engineer", "chemical processes industrial chemistry", "Chemical Engineering"),
("Agricultural Scientist", "agriculture farming crops plants", "Agricultural Science"),
("Wildlife Biologist", "wildlife animals conservation forests", "Wildlife Biology"),
("Nutritionist", "nutrition food diet health", "Nutrition, Food Science"),
("Speech-Language Therapist", "speech language communication disorders", "Speech and Language Therapy"),
("UI UX Designer", "user experience interface app design", "UI UX Design"),
("Ethical Hacker", "ethical hacking cybersecurity networks", "Cybersecurity"),
("Game Artist", "game art characters digital drawing", "Game Art, Animation"),
("Public Relations Specialist", "public relations communication reputation media", "Public Relations"),
("Political Scientist", "politics government democracy society", "Political Science"),
("Librarian", "books libraries reading information", "Library Science"),
("Geologist", "rocks earth minerals geology", "Geology"),
("Oceanographer", "ocean sea currents marine science", "Oceanography"),
("Mathematician", "mathematics equations numbers proofs", "Mathematics"),
("Sociologist", "society social behaviour communities", "Sociology"),
("Philosopher", "philosophy ethics reasoning ideas existence", "Philosophy"),
("Historian", "history past civilizations historical research", "History"),
("Linguist", "languages linguistics grammar speech", "Linguistics"),
("Event Planner", "events organising planning ceremonies", "Event Management"),
("Air Traffic Controller", "air traffic aircraft airport aviation", "Aviation Training"),
("Renewable Energy Engineer", "solar wind renewable energy sustainability", "Energy Engineering"),
("Product Designer", "product design innovation prototypes creativity", "Product Design"),
("Human Resources Specialist", "human resources recruitment people management", "Human Resources"),
("Market Researcher", "market research consumers surveys trends", "Marketing, Research"),
("Criminologist", "crime criminal behaviour criminology research", "Criminology"),
("Cognitive Scientist", "cognition memory thinking mind research", "Cognitive Science"),
("Game Tester", "testing video games gaming quality", "Game Testing, IT"),
("Textile Designer", "textile fabric patterns weaving design", "Textile Design"),
("Makeup Artist", "makeup cosmetics beauty creative", "Cosmetology, Makeup"),
("Emergency Medical Technician", "emergency medical ambulance first aid", "Emergency Medical Care"),
("Urban Planner", "cities urban planning buildings communities", "Urban Planning"),
("Meteorologist", "weather atmosphere climate forecasting", "Meteorology"),
("Science Communicator", "science explaining public speaking writing", "Science Communication"),
("Patent Researcher", "inventions patents innovation intellectual property", "Patent Studies, Law"),
]

if interest.strip():
    words = interest.lower().replace(",", " ").split()
    results = []

    for job in jobs:
        keywords = job[1].lower().split()
        score = sum(1 for word in words if word in keywords)

        if score > 0:
            results.append((score, job))

    results.sort(key=lambda item: item[0], reverse=True)

    st.subheader("🔹 Recommended Jobs:")

    if results:
        for score, job in results:
            st.markdown(f"""
            <div class="job">
                <h3>{job[0].upper()}</h3>
                <p><b>Relevant interests:</b> {job[1]}</p>
                <p><b>Related courses:</b> {job[2]}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No matching jobs found. Try describing your interests with different keywords.")
