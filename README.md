# ML
ML models - sample code

# Links
 * https://www.width.ai/post/bert-for-extractive-text-summarization-on-lectures
 * https://www.width.ai/post/spacy-text-classification
 * https://spacy.io/universe/project/coreferee
 * https://github.com/richardpaulhudson/coreferee#getting-started
 * https://www.width.ai/post/4-long-text-summarization-methods
 * https://www.width.ai/post/gpt3-summarizer
 * https://openai.com/research/summarizing-books
 * https://github.com/amoramine/Pegasus_with_Longformer_summarization
 * https://pypi.org/project/bert-extractive-summarizer/
 * https://github.com/dmmiller612/bert-extractive-summarizer
 * https://github.com/huggingface/neuralcoref
 * https://hub.docker.com/r/openkbs/text-summary-docker
 * https://medium.com/saturdays-ai/building-a-text-summarizer-in-python-using-nltk-and-scikit-learn-class-tfidfvectorizer-2207c4235548
 * https://huggingface.co/docs/transformers/v4.24.0/en/main_classes/pipelines#transformers.SummarizationPipeline
 * https://huggingface.co/facebook/bart-large-cnn?text=The+tower+is+324+metres+%281%2C063+ft%29+tall%2C+about+the+same+height+as+an+81-storey+building%2C+and+the+tallest+structure+in+Paris.+Its+base+is+square%2C+measuring+125+metres+%28410+ft%29+on+each+side.+During+its+construction%2C+the+Eiffel+Tower+surpassed+the+Washington+Monument+to+become+the+tallest+man-made+structure+in+the+world%2C+a+title+it+held+for+41+years+until+the+Chrysler+Building+in+New+York+City+was+finished+in+1930.+It+was+the+first+structure+to+reach+a+height+of+300+metres.+Due+to+the+addition+of+a+broadcasting+aerial+at+the+top+of+the+tower+in+1957%2C+it+is+now+taller+than+the+Chrysler+Building+by+5.2+metres+%2817+ft%29.+Excluding+transmitters%2C+the+Eiffel+Tower+is+the+second+tallest+free-standing+structure+in+France+after+the+Millau+Viaduct
 * https://huggingface.co/docs/transformers/v4.24.0/en/main_classes/pipelines#transformers.Text2TextGenerationPipeline



# How to process long text?
* https://smrzr.io/
Based on these projects, and the attached sample code, build an own solution:
https://github.com/dmmiller612/bert-extractive-summarizer/network/dependents

# Seems like there are 2 pillars of a good summarizer:
1. Coreference technique: identify and substitute the subject of the sentences accurately
2. Extractive Summarization: ability  to cope with long tokens

# Configuration
You can configure the FastAPI framework with WORKERS and THREADS env variable - used by gconf.py