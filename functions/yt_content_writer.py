# functions/yt_content_writer.py

from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def yt_content_writer():
    st.subheader("YouTube Content Writing")

    # Initialize session states
    if "clip_name_ideas" not in st.session_state:
        st.session_state["clip_name_ideas"] = []

    if "selected_clip_name" not in st.session_state:
        st.session_state["selected_clip_name"] = None

    if "manual_clip_name" not in st.session_state:
        st.session_state["manual_clip_name"] = ""

    if "story_points" not in st.session_state:
        st.session_state["story_points"] = []

    if "concise_story" not in st.session_state:
        st.session_state["concise_story"] = None

    if "final_story" not in st.session_state:
        st.session_state["final_story"] = None

    # Step 1: Clip Name Ideas
    clip_name_prompt = st.text_input("1. Please Input the Clip Name", key="clip_name_input")
    
    def generate_clip_name_ideas(prompt):
        messages = [{"role": "system", "content": "Generate 20 concise in clip name ideas from this input. The clip name is in the sentence form by focusing on the mood and feeling or place"}, 
                    {"role": "user", "content": prompt}]
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )
        name_ideas = response.choices[0].message.content.strip().split('\n')
        st.session_state["clip_name_ideas"] = name_ideas

    if st.button("Generate Clip Name Ideas"):
        if clip_name_prompt:
            generate_clip_name_ideas(clip_name_prompt)
    
    if st.session_state["clip_name_ideas"]:
        st.write("Select one of the following clip name ideas:")
        selected_clip_name = st.selectbox("Clip Name Ideas", st.session_state["clip_name_ideas"])
        st.session_state["selected_clip_name"] = selected_clip_name

        if selected_clip_name:
            st.write(f"Selected Clip Name: {selected_clip_name}")
            st.write("Or, input your own clip name below.")

    # Optional manual clip name input
    manual_clip_name = st.text_input("Or, Manually Enter the Clip Name (Optional)", key="manual_clip_name_input")
    st.session_state["manual_clip_name"] = manual_clip_name

    # Determine which clip name to use
    final_clip_name = st.session_state["manual_clip_name"] if st.session_state["manual_clip_name"] else st.session_state["selected_clip_name"]

    # Step 2: Craft a Story
    if final_clip_name:
        story_prompt = st.text_area(
            "2. Please Craft a Story\n- Input: bullet points of main points of the story focusing on mood and feelings",
            key="story_points_input"
        )

        def generate_story(bullets):
            messages = [{
                "role": "system", 
                "content": "Craft a concise story focused on mood and feelings within two paragraphs. Imagine yourself in this isekai anime setting."
            }, {"role": "user", "content": bullets}]

            response = client.chat.completions.create(
                model="gpt-4o",
                messages=messages
            )
            story = response.choices[0].message.content.strip()
            return story

        if st.button("Generate Story"):
            if story_prompt:
                st.session_state["concise_story"] = generate_story(story_prompt)
                st.write(st.session_state["concise_story"])
        
        if st.session_state["concise_story"]:
            feedback = st.text_area("Give feedback to fix the story")
            if st.button("Refine Story"):
                if feedback:
                    # Refine the story based on feedback
                    refined_story = generate_story(feedback)
                    st.session_state["concise_story"] = refined_story
                    st.write(refined_story)

    # Step 3: Generate Final Output
    if st.session_state["concise_story"]:
        if st.button("Proceed to Final Version"):
            if final_clip_name and st.session_state["concise_story"]:
                final_output = (
                    f"🎧 MOOD | {final_clip_name} 🎵 | Isekai Anime Relaxing Music | AMBIENCE\n\n"
                    f"Quest Story:\n{st.session_state['concise_story']}"
                )
                st.session_state["final_story"] = final_output

    if st.session_state["final_story"]:
        st.write("3. Here is the full version for you:")
        st.markdown(st.session_state["final_story"])# functions/yt_content_writer.py

from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def yt_content_writer():
    st.subheader("YouTube Content Writing")

    # Initialize session states
    if "clip_name_ideas" not in st.session_state:
        st.session_state["clip_name_ideas"] = []

    if "selected_clip_name" not in st.session_state:
        st.session_state["selected_clip_name"] = None

    if "manual_clip_name" not in st.session_state:
        st.session_state["manual_clip_name"] = ""

    if "story_points" not in st.session_state:
        st.session_state["story_points"] = []

    if "concise_story" not in st.session_state:
        st.session_state["concise_story"] = None

    if "final_story" not in st.session_state:
        st.session_state["final_story"] = None

    # Step 1: Clip Name Ideas
    clip_name_prompt = st.text_input("1. Please Input the Clip Name", key="clip_name_input")
    
    def generate_clip_name_ideas(prompt):
        messages = [{"role": "system", "content": "Generate 20 concise clip name ideas from this input."}, 
                    {"role": "user", "content": prompt}]
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )
        name_ideas = response.choices[0].message.content.strip().split('\n')
        st.session_state["clip_name_ideas"] = name_ideas

    if st.button("Generate Clip Name Ideas"):
        if clip_name_prompt:
            generate_clip_name_ideas(clip_name_prompt)
    
    if st.session_state["clip_name_ideas"]:
        st.write("Select one of the following clip name ideas:")
        selected_clip_name = st.selectbox("Clip Name Ideas", st.session_state["clip_name_ideas"])
        st.session_state["selected_clip_name"] = selected_clip_name

        if selected_clip_name:
            st.write(f"Selected Clip Name: {selected_clip_name}")
            st.write("Or, input your own clip name below.")

    # Optional manual clip name input
    manual_clip_name = st.text_input("Or, Manually Enter the Clip Name (Optional)", key="manual_clip_name_input")
    st.session_state["manual_clip_name"] = manual_clip_name

    # Determine which clip name to use
    final_clip_name = st.session_state["manual_clip_name"] if st.session_state["manual_clip_name"] else st.session_state["selected_clip_name"]

    # Step 2: Craft a Story
    if final_clip_name:
        story_prompt = st.text_area(
            "2. Please Craft a Story\n- Input: bullet points of main points of the story focusing on mood and feelings",
            key="story_points_input"
        )

        def generate_story(bullets):
            messages = [{
                "role": "system", 
                "content": "Craft a concise story focused on mood and feelings within two paragraphs. Imagine yourself in this isekai anime setting."
            }, {"role": "user", "content": bullets}]

            response = client.chat.completions.create(
                model="gpt-4o",
                messages=messages
            )
            story = response.choices[0].message.content.strip()
            return story

        if st.button("Generate Story"):
            if story_prompt:
                st.session_state["concise_story"] = generate_story(story_prompt)
                st.write(st.session_state["concise_story"])
        
        if st.session_state["concise_story"]:
            feedback = st.text_area("Give feedback to fix the story")
            if st.button("Refine Story"):
                if feedback:
                    # Refine the story based on feedback
                    refined_story = generate_story(feedback)
                    st.session_state["concise_story"] = refined_story
                    st.write(refined_story)

    # Step 3: Generate Final Output
    if st.session_state["concise_story"]:
        if st.button("Proceed to Final Version"):
            if final_clip_name and st.session_state["concise_story"]:
                final_output = (
                    f"🎧 MOOD | {final_clip_name} 🎵 | Isekai Anime Relaxing Music | AMBIENCE\n\n"
                    f"Quest Story:\n{st.session_state['concise_story']}"
                )
                st.session_state["final_story"] = final_output

    if st.session_state["final_story"]:
        st.write("3. Here is the full version for you:")
        st.markdown(st.session_state["final_story"])