import gradio as gr
import sys
import os

# Add project root to path
PROJECT_ROOT = os.path.abspath("..")
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from embeddings.query_faiss import search_gita
from reasoning.llm_reasoning import reason_over_verses

# ========================================================================
# HELPER FUNCTIONS
# ========================================================================

def format_verse_card(verse, index=1):
    """Format a single verse as HTML card"""
    
    score_stars = "⭐" * min(5, int(verse['score'] * 5))
    themes = ", ".join(verse.get('themes', [])[:3]) if verse.get('themes') else "General wisdom"
    
    return f"""
    <div style="
        background: white;
        padding: 20px;
        border-radius: 15px;
        margin: 15px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    ">
        <h3 style="color: #2C3E50; margin-top: 0;">
            📖 Verse {index}: Chapter {verse['chapter']}, Verse {verse['verse']}
        </h3>
        
        <div style="
            display: inline-block;
            background: #28a745;
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 14px;
            margin-bottom: 15px;
        ">
            Score: {verse['score']:.2f} {score_stars}
        </div>
        
        <div style="margin-bottom: 10px;">
            <strong>🏷️ Themes:</strong> {themes}
        </div>
        
        <div style="
            background: #FFF8DC;
            padding: 15px;
            border-radius: 10px;
            border-left: 4px solid #DAA520;
            margin: 15px 0;
        ">
            <strong style="color: #8B4513;">📜 Sanskrit:</strong><br>
            <span style="
                font-family: 'Noto Sans Devanagari', serif;
                font-size: 18px;
                color: #8B4513;
                line-height: 1.8;
            ">{verse['sanskrit']}</span>
        </div>
        
        <div style="
            background: #F0F8FF;
            padding: 15px;
            border-radius: 10px;
            border-left: 4px solid #4682B4;
        ">
            <strong style="color: #2C3E50;">🌍 English:</strong><br>
            <span style="color: #2C3E50; line-height: 1.6;">{verse['english']}</span>
        </div>
    </div>
    """


def format_guidance_box(guidance_text):
    """Format AI guidance in styled box"""
    
    return f"""
    <div style="
        background: linear-gradient(135deg, #FFF8DC 0%, #FFE4B5 100%);
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #DAA520;
        margin: 20px 0;
    ">
        <h3 style="color: #8B4513; margin-top: 0;">🪔 Personalized Guidance</h3>
        <div style="color: #2C3E50; line-height: 1.8; white-space: pre-wrap;">
{guidance_text}
        </div>
    </div>
    """


def process_query(user_question):
    """Main function to process user query and return formatted results"""
    
    if not user_question.strip():
        return "⚠️ Please enter your question.", "", ""
    
    try:
        # Search for verses
        results = search_gita(user_question)
        
        if not results:
            return "❌ No relevant verses found. Please rephrase your question.", "", ""
        
        # Get AI guidance
        guidance = reason_over_verses(user_question, results)
        
        # Format primary verse (most relevant)
        primary_verse_html = format_verse_card(results[0], index=1)
        
        # Format guidance
        guidance_html = format_guidance_box(guidance)
        
        # Format other verses
        other_verses_html = "<h3>📚 Other Relevant Verses</h3>"
        for i, verse in enumerate(results[1:], 2):
            other_verses_html += format_verse_card(verse, index=i)
        
        # Combine all sections
        full_output = f"""
        <div style="max-width: 1200px; margin: 0 auto;">
            <h2 style="color: #2C3E50; border-bottom: 3px solid #DAA520; padding-bottom: 10px;">
                📖 Selected Verse (Highest Match)
            </h2>
            {primary_verse_html}
            
            {guidance_html}
            
            <hr style="margin: 40px 0; border: none; border-top: 2px solid #E0E0E0;">
            
            {other_verses_html}
        </div>
        """
        
        return full_output
        
    except Exception as e:
        error_message = f"""
        <div style="background: #FFE5E5; padding: 20px; border-radius: 10px; border-left: 4px solid #D32F2F;">
            <h3 style="color: #D32F2F; margin-top: 0;">❌ Error</h3>
            <p>{str(e)}</p>
            <p><strong>Troubleshooting:</strong></p>
            <ul>
                <li>Check if GROQ_API_KEY is set</li>
                <li>Verify internet connection</li>
                <li>Ensure all dependencies are installed</li>
            </ul>
        </div>
        """
        return error_message


# ========================================================================
# GRADIO INTERFACE
# ========================================================================

# Example questions for quick selection
examples = [
    ["I feel confused and afraid about my future"],
    ["I'm struggling with anger towards someone"],
    ["How do I handle a difficult decision at work?"],
    ["I feel stuck and unmotivated in life"],
    ["How do I deal with grief and loss?"],
]

# Custom CSS
custom_css = """
#component-0 {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.gradio-container {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@400;700&display=swap');
"""

# Create interface
with gr.Blocks(css=custom_css, theme=gr.themes.Soft()) as app:
    
    gr.Markdown("""
    # 🪔 Gita Guidance
    ### Ancient Wisdom for Modern Life
    
    Share your concerns and receive personalized guidance from the Bhagavad Gita, 
    interpreted by AI for modern context.
    """)
    
    with gr.Row():
        with gr.Column(scale=2):
            user_input = gr.Textbox(
                label="💭 What's troubling you?",
                placeholder="Share what's on your mind... For example: 'I feel anxious about an upcoming job interview' or 'I'm struggling to balance work and family'",
                lines=4
            )
            
            submit_btn = gr.Button("🔍 Seek Guidance", variant="primary", size="lg")
    
    gr.Markdown("### 💡 Example Questions (click to use)")
    gr.Examples(
        examples=examples,
        inputs=user_input,
        label="Quick Start"
    )
    
    gr.Markdown("---")
    
    output = gr.HTML(label="Results")
    
    # Connect button to function
    submit_btn.click(
        fn=process_query,
        inputs=user_input,
        outputs=output
    )
    
    # Also submit on Enter key
    user_input.submit(
        fn=process_query,
        inputs=user_input,
        outputs=output
    )
    
    gr.Markdown("""
    ---
    ### 🙏 About This App
    
    This app combines:
    - **Semantic Search** (FAISS) to find relevant verses
    - **AI Reasoning** (Groq/Llama) to provide personalized guidance
    - **700+ verses** from the Bhagavad Gita
    
    **Tips for best results:**
    - Be specific about your situation
    - Focus on one challenge at a time
    - Ask about real problems you're facing
    
    ---
    *Built with reverence for ancient wisdom and modern technology*  
    *The Bhagavad Gita is a sacred Hindu scripture. This app is for educational purposes.*
    """)

# ========================================================================
# LAUNCH
# ========================================================================

if __name__ == "__main__":
    app.launch(
        share=True,  # Creates public link
        server_name="0.0.0.0",
        server_port=7860
    )