import argparse
from collections import Counter
import os
import re

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Word Count CLI Tool - Analyze word frequencies in a text file."
    )
    parser.add_argument("file", type=str, help="Path to the text file to analyze")
    parser.add_argument("--top", type=int, default=10, help="Number of top words to display (default: 10)")
    parser.add_argument("--min-length", type=int, default=1, help="Minimum word length to include (default: 1)")
    parser.add_argument("--ignore-case", action="store_true", help="Ignore letter case")
    
    return parser.parse_args()


def analyze_file(file_path, top, min_length, ignore_case):
    # 1. בדיקה שהקובץ קיים
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    # 2. קריאת הקובץ
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # 3. טיפול ב-Case במידת הצורך
    if ignore_case:
        text = text.lower()

    # 4. חילוץ מילים (בעזרת Regex שמנקה סימני פיסוק)
    words = re.findall(r'\b\w+\b', text)

    # 5. סינון מילים לפי אורך מינימלי
    filtered_words = [w for w in words if len(w) >= min_length]

    # 6. ספירת תדירויות
    word_counts = Counter(filtered_words)

    # 7. הדפסת התוצאות
    print(f"\n--- Word Count Results for '{file_path}' ---")
    print(f"Total words found: {len(words)}")
    print(f"Unique words (min length {min_length}): {len(word_counts)}")
    print(f"Top {top} words:\n")

    for word, count in word_counts.most_common(top):
        print(f"{word:<20} : {count}")


if __name__ == "__main__":
    args = parse_arguments()
    analyze_file(args.file, args.top, args.min_length, args.ignore_case)