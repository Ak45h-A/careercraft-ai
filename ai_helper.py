import anthropic
import streamlit as st

def get_client():
    api_key = st.session_state.get("api_key", "")
    if not api_key:
        return None
    return anthropic.Anthropic(api_key=api_key)

def call_ai(prompt: str, system: str = "You are a professional career consultant and resume expert.", max_tokens: int = 2000) -> str:
    client = get_client()
    if not client:
        return "❌ Please add your Anthropic API key in Settings first."
    try:
        message = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": prompt}]
        )
        return message.content[0].text
    except Exception as e:
        return f"❌ AI Error: {str(e)}"

def profile_to_text(p: dict) -> str:
    """Convert profile dict to readable text for AI prompts"""
    lines = []
    if p.get("name"): lines.append(f"Name: {p['name']}")
    if p.get("email"): lines.append(f"Email: {p['email']}")
    if p.get("phone"): lines.append(f"Phone: {p['phone']}")
    if p.get("city"): lines.append(f"Location: {p.get('city')}, {p.get('state','')}")
    if p.get("summary"): lines.append(f"Summary: {p['summary']}")
    if p.get("total_experience"): lines.append(f"Total Experience: {p['total_experience']}")

    if p.get("experiences"):
        lines.append("\nWORK EXPERIENCE:")
        for exp in p["experiences"]:
            if exp.get("title"):
                lines.append(f"  - {exp.get('title')} at {exp.get('company','')}, {exp.get('start','')} to {exp.get('end','')}")
                if exp.get("description"):
                    lines.append(f"    {exp['description']}")

    if p.get("education"):
        lines.append("\nEDUCATION:")
        for edu in p["education"]:
            if edu.get("degree"):
                lines.append(f"  - {edu.get('degree')} from {edu.get('institution','')}, {edu.get('year','')}, {edu.get('grade','')}")

    if p.get("technical_skills"): lines.append(f"\nTechnical Skills: {p['technical_skills']}")
    if p.get("soft_skills"): lines.append(f"Soft Skills: {p['soft_skills']}")
    if p.get("tools"): lines.append(f"Tools: {p['tools']}")
    if p.get("certifications"): lines.append(f"Certifications: {p['certifications']}")
    if p.get("projects"): lines.append(f"\nProjects:\n{p['projects']}")
    if p.get("achievements"): lines.append(f"\nAchievements:\n{p['achievements']}")
    if p.get("linkedin"): lines.append(f"\nLinkedIn: {p['linkedin']}")
    if p.get("github"): lines.append(f"GitHub: {p['github']}")

    return "\n".join(lines)
