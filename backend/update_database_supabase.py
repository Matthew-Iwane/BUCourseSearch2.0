from dotenv import load_dotenv
import os
from supabase import create_client, Client
from webscrape import grab_search_data

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")


supabase: Client = create_client(url, key)

data = grab_search_data()

sections_list = []

for course in data:
    sections_list.extend(course.pop("sections"))

# data = [{'course_id': 'CAS AA 103', 'college': 'CAS', 'department': 'AA', 'course': '103', 'name': 'Introduction to African American Literature', 'description': 'What is the African American literary tradition? In this course, we will read   poetry, slave narratives, essays, speeches, tales, short stories, and novels and   consider how culture, politics, and history shape African American literature.   Carries humanities divisional credit in CAS.  Effective Fall 2018,  this course fulfills a  single unit in each of the  following BU Hub areas: Aesthetic  Exploration,  Global Citizenship and  Intercultural Literacy. Effective Fall 2019, this   course fulfills a single unit in each of the  following BU Hub areas: Aesthetic   Exploration, Global Citizenship and  Intercultural Literacy, Critical Thinking. Effective Fall 2022, this course  fulfills a single unit in each of the following BU Hub areas: Writing-Intensive  Course, Global Citizenship and Intercultural Literacy, Critical Thinking.', 'prereqs': 'Prereq: First-Year Writing Seminar (WR 120 or equivalent)', 'credits': 4, 'hubs': ['Global Citizenship and Intercultural Literacy', 'Critical Thinking', 'Writing-Intensive Course', 'BU Hub Pathway:\xa0\xa0Social & Racial Justice'], 'professors': ['Maryanne Boelcskevy']}, {'course_id': 'CAS AA 112', 'college': 'CAS', 'department': 'AA', 'course': '112', 'name': 'Black Power in the Classroom: The History of Black Studies', 'description': 'Centers Black experiences, cultures, knowledge production and identity   formation in the United States and in the African Diaspora across time and   space. Examines and traces the genealogies of Black Studies as a discipline:   its political, ideological, and practical foundations on college campuses  and  in communities. Also explores earlier traditions and contemporary work  in Black  radical thought and activism that lay the groundwork for and build  on the  founding principles of Black Studies by mobilizing an intersectional  and  diasporic lens.  Effective Fall 2020, this course fulfills a single  unit in each of the following BU Hub areas: Historical Consciousness, Social  Inquiry I, Research and Information Literacy.', 'prereqs': '', 'credits': 4, 'hubs': ['Historical Consciousness', 'Social Inquiry I', 'Research and Information Literacy', 'BU Hub Pathway:\xa0\xa0Social & Racial Justice'], 'professors': ['Aminah Pilgrim']}, {'course_id': 'CAS AA 207', 'college': 'CAS', 'department': 'AA', 'course': '207', 'name': 'Sociology of Race and Ethnicity', 'description': 'Examines the fundamental theoretical and empirical approaches regarding  race/ethnicity and the current state of race relations in the U.S. that explore  both contemporary social problems. Effective Fall 2019,  this  course  fulfills a  single unit in each of the following BU Hub areas:   Historical  Consciousness,  The Individual in Community, Research and  Information  Literacy. ', 'prereqs': '', 'credits': 4, 'hubs': ['Historical Consciousness', 'The Individual in Community', 'Research and Information Literacy', 'BU Hub Pathway:\xa0\xa0Social & Racial Justice'], 'professors': ['Saida Grundy']}, {'course_id': 'CAS AA 215', 'college': 'CAS', 'department': 'AA', 'course': '215', 'name': 'Arts of Africa and Its Diaspora', 'description': 'Exploration of a diversity of visual and performing arts from Africa,    including  royal regalia,  masquerades, and contemporary painting. Examines    how the  dispersal of Africans, due to the  transatlantic slave trade and    immigration,  contributed to the cultural richness of the Americas. Effective  Fall 2019, this   course  fulfills a single unit in each of the following BU Hub  areas:   Aesthetic   Exploration, Global Citizenship and Intercultural Literacy,   Critical  Thinking. ', 'prereqs': '', 'credits': 4, 'hubs': ['Aesthetic Exploration', 'Global Citizenship and Intercultural Literacy', 'Critical Thinking', 'BU Hub Pathway:\xa0\xa0Social & Racial Justice'], 'professors': ['Sarah Clunis']}, {'course_id': 'CAS AA 234', 'college': 'CAS', 'department': 'AA', 'course': '234', 'name': 'African Americans in Global Perspective: Slavery and the Creation of Race', 'description': 'A study of how chattel slavery in the Americas led to racialization as a  primary  tool in the creation of American society and New World capitalism.   Effective Fall 2020, this course fulfills a single unit in each of the  following BU Hub areas: Ethical Reasoning, Global Citizenship and  Intercultural Literacy, Critical Thinking.', 'prereqs': '', 'credits': 4, 'hubs': ['Global Citizenship and Intercultural Literacy', 'Ethical Reasoning', 'Critical Thinking', 'BU Hub Pathway:\xa0\xa0Social & Racial Justice'], 'professors': ['Joyce Scott']}, {'course_id': 'CAS AA 296', 'college': 'CAS', 'department': 'AA', 'course': '296', 'name': 'Religion and Hip Hop', 'description': 'Uses digital media studies to explore diverse religious expressions in hip  hop  culture. Through critical reading, community field trips, and hands-on   technology usage, students consider an often overlooked element in the study   of hip hop culture: religion. Effective Fall 2020, this course fulfills a  single unit in each of the following BU Hub areas: Digital/Multimedia  Expression, Aesthetic Exploration, Creativity/Innovation.', 'prereqs': '', 'credits': 4, 'hubs': ['Aesthetic Exploration', 'Digital/Multimedia Expression', 'Creativity/Innovation', 'BU Hub Pathway:\xa0\xa0Social & Racial Justice'], 'professors': ['Margarita Guillory']}, {'course_id': 'CAS AA 308', 'college': 'CAS', 'department': 'AA', 'course': '308', 'name': 'Race and Politics', 'description': 'Combining research from history, political science, sociology, and economics,  this course examines the role of race and ethnicity in shaping American  politics and policy. Effective Fall 2019, this course fulfills a single unit  in each of the following BU Hub areas: Social Inquiry II, Ethical Reasoning,  Critical Thinking.', 'prereqs': '', 'credits': 4, 'hubs': ['Ethical Reasoning', 'Social Inquiry II', 'Critical Thinking', 'BU Hub Pathway:\xa0\xa0Social & Racial Justice'], 'professors': [nan]}, {'course_id': 'CAS AA 310', 'college': 'CAS', 'department': 'AA', 'course': '310', 'name': 'Civil Rights History', 'description': 'This course examines the U.S. Civil Rights and the struggle for black  freedom movements. From the late nineteenth century through the twenty-first  century, we consider events, organizations, "leaders" and organizers, legal  campaigns, and political protests to answer the questions: What were the  race, class, and gender dynamics within the movements? What were the  changing definitions of freedom? The course treats the movement\'s roots,  goals, ideologies, and cultures, and includes a comparison of the struggles  for equal rights of Mexican Americans, Native Americans, LGBT folks, and  other groups.  Effective Spring 2021, this course fulfills a single unit in  each of the following BU Hub areas: The Individual in Community, Historical  Consciousness, Teamwork/Collaboration.', 'prereqs': '', 'credits': 4, 'hubs': ['Historical Consciousness', 'The Individual in Community', 'Teamwork/Collaboration', 'BU Hub Pathway:\xa0\xa0Social & Racial Justice'], 'professors': ['Aminah Pilgrim']}, {'course_id': 'CAS AA 335', 'college': 'CAS', 'department': 'AA', 'course': '335', 'name': 'Sociology of Race, Class & Gender', 'description': 'No one of us is one thing, one identity, nor motivated by one singular interest,  nor privileged or subjugated by one singular form of power, but how do those  multiple forms of ourselves affect how we are advantaged, disadvantaged, viewed,  and understood by the social world? Our social world, is, by default, a vast web  of social intersections between and across groups with shared, overlapping, and  conflicting identities. Race, class and gender affect nearly all of our lived  experiences and greatly complicate and nuance concepts of diversity and  difference. Effective Fall 2020, this course   fulfills a single unit in each of  the following BU Hub areas:   Digital/Multimedia Expression , The Individual in  Community, Historical   Consciousness.', 'prereqs': 'Prereq: At least one prior 100- or 200-level sociology course, or CAS WS 101/102.', 'credits': 4, 'hubs': ['Historical Consciousness', 'The Individual in Community', 'Digital/Multimedia Expression', 'BU Hub Pathway:\xa0\xa0Social & Racial Justice'], 'professors': ['Saida Grundy']}, {'course_id': 'CAS AA 356', 'college': 'CAS', 'department': 'AA', 'course': '356', 'name': 'Religion in the Digital Age', 'description': 'How has technology impacted religion? This hands-on course explores how digital  technologies like the Internet, social media, gaming, and artificial intelligence  have changed the way that people think about religion.  Effective Spring 2022,  this course fulfills a single unit in each of the following BU Hub areas:  Digital/Multimedia Expression, Writing-Intensive Course, Creativity/Innovation.', 'prereqs': 'Prereq: First-Year Writing Seminar (CAS WR 120 or equivalent)', 'credits': 4, 'hubs': ['Digital/Multimedia Expression', 'Creativity/Innovation', 'Writing-Intensive Course'], 'professors': ['Margarita Guillory']}]
# sections_list = [{'section_full_name': 'CAS AA 103 A1', 'course_id': 'CAS AA 103', 'section': 'A1', 'instructor': 'Maryanne Boelcskevy', 'instructorDiff': -1, 'instructorRating': -1, 'type': 'IND', 'location': 'CAS 214', 'days': 'MWF', 'scheduleStart': 610, 'scheduleEnd': 660, 'availability': False}, {'section_full_name': 'CAS AA 112 A1', 'course_id': 'CAS AA 112', 'section': 'A1', 'instructor': 'Aminah Pilgrim', 'instructorDiff': 2.2, 'instructorRating': 4.3, 'type': 'IND', 'location': 'SOC B63', 'days': 'TR', 'scheduleStart': 750, 'scheduleEnd': 825, 'availability': False}, {'section_full_name': 'CAS AA 207 A1', 'course_id': 'CAS AA 207', 'section': 'A1', 'instructor': 'Saida Grundy', 'instructorDiff': 3.0, 'instructorRating': 4.7, 'type': 'LEC', 'location': 'FLR 205', 'days': 'TR', 'scheduleStart': 570, 'scheduleEnd': 645, 'availability': False}, {'section_full_name': 'CAS AA 207 A2', 'course_id': 'CAS AA 207', 'section': 'A2', 'instructor': 'Saida Grundy', 'instructorDiff': 2.9, 'instructorRating': 4.7, 'type': 'DIS', 'location': 'CAS 320', 'days': 'W', 'scheduleStart': 545, 'scheduleEnd': 595, 'availability': False}, {'section_full_name': 'CAS AA 207 A3', 'course_id': 'CAS AA 207', 'section': 'A3', 'instructor': 'Saida Grundy', 'instructorDiff': 2.9, 'instructorRating': 4.7, 'type': 'DIS', 'location': 'FLR 122', 'days': 'W', 'scheduleStart': 610, 'scheduleEnd': 660, 'availability': False}, {'section_full_name': 'CAS AA 207 A4', 'course_id': 'CAS AA 207', 'section': 'A4', 'instructor': 'Saida Grundy', 'instructorDiff': 2.9, 'instructorRating': 4.7, 'type': 'DIS', 'location': 'PSY B37', 'days': 'W', 'scheduleStart': 740, 'scheduleEnd': 790, 'availability': False}, {'section_full_name': 'CAS AA 215 A1', 'course_id': 'CAS AA 215', 'section': 'A1', 'instructor': 'Sarah Clunis', 'instructorDiff': 3.7, 'instructorRating': 3.2, 'type': 'IND', 'location': 'SOC B63', 'days': 'TR', 'scheduleStart': 1020, 'scheduleEnd': 1095, 'availability': False}, {'section_full_name': 'CAS AA 234 A1', 'course_id': 'CAS AA 234', 'section': 'A1', 'instructor': 'Joyce Scott', 'instructorDiff': 3.4, 'instructorRating': 3.4, 'type': 'IND', 'location': 'AAS 102', 'days': 'TR', 'scheduleStart': 570, 'scheduleEnd': 645, 'availability': False}, {'section_full_name': 'CAS AA 296 A1', 'course_id': 'CAS AA 296', 'section': 'A1', 'instructor': 'Margarita Guillory', 'instructorDiff': 3.0, 'instructorRating': 5.0, 'type': 'IND', 'location': 'CAS 326', 'days': 'TR', 'scheduleStart': 570, 'scheduleEnd': 645, 'availability': False}, {'section_full_name': 'CAS AA 308 A1', 'course_id': 'CAS AA 308', 'section': 'A1', 'instructor': 'None', 'instructorDiff': -1, 'instructorRating': -1, 'type': 'IND', 'location': 'CAS B36', 'days': 'MWF', 'scheduleStart': 610, 'scheduleEnd': 660, 'availability': False}, {'section_full_name': 'CAS AA 310 A1', 'course_id': 'CAS AA 310', 'section': 'A1', 'instructor': 'Aminah Pilgrim', 'instructorDiff': 2.0, 'instructorRating': 5.0, 'type': 'IND', 'location': 'CAS B36', 'days': 'TR', 'scheduleStart': 660, 'scheduleEnd': 735, 'availability': False}, {'section_full_name': 'CAS AA 335 A1', 'course_id': 'CAS AA 335', 'section': 'A1', 'instructor': 'Saida Grundy', 'instructorDiff': 3.0, 'instructorRating': 4.7, 'type': 'IND', 'location': 'PSY B53', 'days': 'T', 'scheduleStart': 750, 'scheduleEnd': 915, 'availability': False}, {'section_full_name': 'CAS AA 356 A1', 'course_id': 'CAS AA 356', 'section': 'A1', 'instructor': 'Margarita Guillory', 'instructorDiff': 3.0, 'instructorRating': 5.0, 'type': 'IND', 'location': 'CAS 228', 'days': 'TR', 'scheduleStart': 750, 'scheduleEnd': 825, 'availability': False}]

try:
    # code runs into simplejson.decoder.JSONDecodeError after successfuly uploading to db
    # no idea why this occurs, but we need this try except for the 2nd method to run as well
    supabase.table("Courses").insert(data).execute()
except ValueError:
    pass

try:
    supabase.table("Sections").insert(sections_list).execute()
except ValueError:
    pass

print("program successful!")
