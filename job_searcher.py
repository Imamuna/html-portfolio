Python




import requests
import json

def fetch_global_remote_jobs():
    print("🛰️ Connecting to Global Remote Job Boards...")
    # Using Remotive's public API
    url = "https://remotive.com/api/remote-jobs"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            all_jobs = data.get('jobs', [])
            print(f"📥 Successfully fetched {len(all_jobs)} total remote roles. Filtering targets...")
            filter_my_roles(all_jobs)
        else:
            print(f"❌ Failed to fetch jobs. Server responded with code: {response.status_code}")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")

def filter_my_roles(jobs):
    # Criteria tailored for Michael's profile
    target_keywords = ["customer success", "technical support", "support engineer", "account management"]
    matched_jobs = []

    for job in jobs:
        title = job.get('title', '').lower()
        category = job.get('category', '').lower()
        location = job.get('candidate_required_location', '').lower()
        
        # Ensure the job matches target fields AND allows global candidates (Worldwide/Anywhere)
        is_target_role = any(keyword in title or keyword in category for keyword in target_keywords)
        is_global_remote = "worldwide" in location or "anywhere" in location or "global" in location

        if is_target_role and is_global_remote:
            matched_jobs.append({
                "Title": job.get('title'),
                "Company": job.get('company_name'),
                "Location Requirements": job.get('candidate_required_location'),
                "Salary / Comp": job.get('salary', 'Not specified (Check description for $50k+ brackets)'),
                "URL": job.get('url')
            })

    # Output Results
    print(f"\n🎯 Found {len(matched_jobs)} Global Remote Roles matching your criteria:\n")
    print("=" * 80)
    for index, match in enumerate(matched_jobs[:15], 1): # Displaying top 15 results
        print(f"{index}. {match['Title']} at {match['Company']}")
        print(f"   🌍 Location: {match['Location Requirements']}")
        print(f"   💰 Comp Range: {match['Salary / Comp']}")
        print(f"   🔗 Apply Link: {match['URL']}")
        print("-" * 80)

if __name__ == "__main__":
    fetch_global_remote_jobs()
