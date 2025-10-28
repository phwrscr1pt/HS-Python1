lyrics = """
[Intro]
Desert you
Ooh-ooh-ooh-ooh
Hurt you

[Verse 1]
We're no strangers to love
You know the rules and so do I (Do I)
A full commitment's what I'm thinking of
You wouldn't get this from any other guy

[Pre-Chorus]
I just wanna tell you how I'm feeling
Gotta make you understand

[Chorus]
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

[Verse 2]
We've known each other for so long
Your heart's been aching, but you're too shy to say it (To say it)
Inside, we both know what's been going on (Going on)
We know the game, and we're gonna play it

[Pre-Chorus]
And if you ask me how I'm feeling
Don't tell me you're too blind to see

[Chorus]
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

[Bridge]
Ooh (Give you up)
Ooh-ooh (Give you up)
Ooh-ooh
Never gonna give, never gonna give (Give you up)
Ooh-ooh
Never gonna give, never gonna give (Give you up)
[Verse 3]
We've known each other for so long
Your heart's been aching, but you're too shy to say it (To say it)
Inside, we both know what's been going on (Going on)
We know the game, and we're gonna play it

[Pre-Chorus]
I just wanna tell you how I'm feeling
Gotta make you understand

[Chorus]
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
"""

lyrics_modified = ""

# Count the number of times "never gonna"/"Never gonna" appears in the lyrics
number_of_word = lyrics_modified.count("Never gonna")

# Remove the section separator, suchas [intro], [Verse1], etc...
lyrics_modified = lyrics.replace("[Intro]", "")
lyrics_modified = lyrics_modified.replace("[Verse 1]", "")
lyrics_modified = lyrics_modified.replace("[Verse 2]", "")
lyrics_modified = lyrics_modified.replace("[Verse 3]", "")
lyrics_modified = lyrics_modified.replace("[Bridge]", "")
lyrics_modified = lyrics_modified.replace("[Pre-Chorus]", "")
lyrics_modified = lyrics_modified.replace("[Chorus]", "")

# How many lines of lyrics, after doing 2., are there?
count_line_of_modified_lyrics = lyrics_modified.split("\n")
# print(count_line_of_modified_lyrics)
print(len(count_line_of_modified_lyrics))

# How many number of alphabets are there in the lyrics?
count_alphabests = 0
for index in lyrics:
    if index.isalpha() :
        count_alphabests += 1

print(count_alphabests)