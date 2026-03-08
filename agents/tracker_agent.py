from memory.journal_db import save_entry, get_entries

class WellnessTrackerAgent:

    def save_journal(self, mood, text):
        save_entry(mood, text)

    def get_history(self):
        return get_entries()

    def calculate_average_mood(self):

        entries = get_entries()

        if not entries:
            return None

        moods = [e["mood"] for e in entries]

        return sum(moods) / len(moods)