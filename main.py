import requests, random, time

def logo():
    with open("logo.txt", "r") as l:
        print(l.read())

def get_user_agents():
    with open("user_agents.txt", "r") as f:
        return [ua.strip() for ua in f.readlines() if ua.strip()]

def watch_video(url, user_agents):
    headers = {
        "User-Agent": random.choice(user_agents),
        "Accept-Language": "en-US,en;q=0.9",
    }
    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            print("[✓] View sent to:", url)
        else:
            print("[x] Failed to send view")
    except:
        print("[x] Error sending view")

def main():
    logo()
    user_agents = get_user_agents()
    url = input("Enter YouTube Video URL: ")
    views = int(input("How many views to send?: "))
    for i in range(views):
        watch_video(url, user_agents)
        time.sleep(random.uniform(5, 10))  # delay to mimic human

if __name__ == "__main__":
    main()
