from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def perform_topic_modeling(data, text_column='headline', n_topics=5, n_words=10):

    # Ensure the column exists
    if text_column not in data.columns:
        raise ValueError(f"Column '{text_column}' does not exist in the dataset.")
    
    # Preprocess and vectorize the text
    vectorizer = CountVectorizer(stop_words='english')
    doc_term_matrix = vectorizer.fit_transform(data[text_column])

    # Apply LDA
    lda_model = LatentDirichletAllocation(n_components=n_topics, random_state=42)
    lda_model.fit(doc_term_matrix)

    # Get the top words for each topic
    words = vectorizer.get_feature_names_out()
    topics = []
    for topic_idx, topic in enumerate(lda_model.components_):
        top_words = [words[i] for i in topic.argsort()[-n_words:][::-1]]
        topics.append(top_words)

    return topics