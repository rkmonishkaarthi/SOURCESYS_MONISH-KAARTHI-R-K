from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

text = """India is currently experiencing a wave of transformative trends driven by rapid digitalization, 
a young population, and evolving economic priorities. One of the most prominent shifts is the widespread 
adoption of digital payments through platforms like Unified Payments Interface (UPI), which has revolutionized 
how people transact, from small street vendors to large businesses. Alongside this, the startup ecosystem has 
expanded significantly, with cities like Bengaluru, Hyderabad, and Pune emerging as innovation hubs, especially 
in sectors like fintech, edtech, and healthtech. Artificial intelligence and data-driven technologies are 
increasingly being integrated into everyday applications, from personalized recommendations to smart governance 
initiatives. Another key trend is the push toward renewable energy, with India investing heavily in solar and wind 
power to reduce dependence on fossil fuels and meet sustainability goals. The rise of remote and hybrid work culture,
accelerated after the pandemic, has also reshaped urban living and job markets, enabling professionals to work from 
smaller towns while contributing to global companies. Additionally, there is a growing emphasis on local manufacturing 
through initiatives like Make in India, encouraging domestic production and reducing import dependency. Social trends 
are also evolving, with increased awareness around mental health, fitness, and sustainable living, especially among 
younger generations. Altogether, these trends reflect a rapidly modernizing nation that is balancing technological 
advancement with cultural and economic shifts, positioning India as a key player in the global landscape.
"""

result = summarizer(text, max_length=50, min_length=20)

print(result)