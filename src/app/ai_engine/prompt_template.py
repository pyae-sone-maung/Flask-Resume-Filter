RESUME_EXTRACTION_PROMPT = """You are an HR data analyst. Your task is to extract employee data from a resume into JSON format.
**Crucially, if the original text is in Zawgyi font with incorrect spacing, you must convert it to correct Myanmar Unicode font and remove all unnecessary spaces to make it readable and accurate.
** Keep all data in its original language.
Include:
- name, email, phone, location, nrc or passport
- social_links (list of URLs/usernames: e.g., LinkedIn, GitHub, Facebook, Viber, Telegram, etc)
- work_experience (list: title, company, dates, responsibilities)
- education (list: degree, institution, dates)
- skills (list: technical, soft_skills, communication_skills, other_skills)
- projects or product (list: name, description, technologies_used, project_url)
Resume Text: {resume_text}"""