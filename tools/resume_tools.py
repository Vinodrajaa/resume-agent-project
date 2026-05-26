import json
import os

FILE_PATH = "data/resume.json"


# ---------------- LOAD / SAVE ----------------

def load_resume():

    if not os.path.exists(FILE_PATH):

        return {
            "summary": "",
            "skills": [],
            "experiences": [],
            "educations": [],
            "projects": []
        }

    with open(FILE_PATH, "r") as file:
        return json.load(file)


def save_resume(data):

    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)


# ---------------- READ TOOLS ----------------

def get_resume():

    return load_resume()


def get_section(section_name):

    data = load_resume()

    return data.get(section_name, [])


# ---------------- SKILLS TOOLS ----------------

def add_skill(skill):

    data = load_resume()

    skill = skill.upper()

    if skill not in data["skills"]:

        data["skills"].append(skill)

        save_resume(data)

    return f"{skill} added successfully"


def remove_skill(skill):

    data = load_resume()

    skill = skill.upper()

    if skill in data["skills"]:

        data["skills"].remove(skill)

        save_resume(data)

    return f"{skill} removed successfully"


# ---------------- SUMMARY TOOLS ----------------

def update_summary(summary):

    data = load_resume()

    data["summary"] = summary

    save_resume(data)

    return "Summary updated successfully"


# ---------------- EXPERIENCE TOOLS ----------------

def add_experience_bullet(exp_id, bullet):

    data = load_resume()

    for exp in data["experiences"]:

        if exp["id"] == exp_id:

            if "bullets" not in exp:
                exp["bullets"] = []

            exp["bullets"].append(bullet)

    save_resume(data)

    return "Experience bullet added successfully"


def update_experience(exp_id, role=None, company=None):

    data = load_resume()

    for exp in data["experiences"]:

        if exp["id"] == exp_id:

            if role:
                exp["role"] = role

            if company:
                exp["company"] = company

    save_resume(data)

    return "Experience updated successfully"


# ---------------- EDUCATION TOOLS ----------------

def update_education(education_id, degree):

    data = load_resume()

    for edu in data["educations"]:

        if edu["id"] == education_id:

            edu["degree"] = degree

    save_resume(data)

    return "Education updated successfully"


# ---------------- PROJECT TOOLS ----------------

def add_project(title, description):

    data = load_resume()

    project = {
        "id": len(data["projects"]) + 1,
        "title": title,
        "description": description
    }

    data["projects"].append(project)

    save_resume(data)

    return "Project added successfully"


def remove_project(title):

    data = load_resume()

    data["projects"] = [

        project
        for project in data["projects"]
        if project["title"].lower() != title.lower()

    ]

    save_resume(data)

    return "Project removed successfully"