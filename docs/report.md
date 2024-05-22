1. Introduction 
    - What is the system? 
      - Zeeguu API -> Zeeguu is a software for giving directions to people learning second languages to enhance their learning experience at speed.
    - What is the problem? (e.g. most architecturally relevant modules? most architecturally relevant classes? etc.)
      - This will be deducted from the diagrams created using the tools
2. Methodology
    - Tool support: did you use any off-the shelf tools? Your own scripts? 
      - I wanted to see what tools were available out there so I wrote some scripts that used pre existing tools which can be run using the main.py file in this directory. Instructions are available both with commands and in the documentation of the file.
    - Data gathering: what sources of data did you use? Source viewpoints? Reverse engineering patterns? 
      - ???
    - Knowledge inference: did you use any abstraction approach? What target viewpoint do you want to recover?( the architectural viewpoints can be the ones we discuss in the lectures, or you can design your own; I'm happy to see your creativity in action. If you want to create a new viewpoint, but you're not sure about it, discuss with us)
      - Model viewpoint from 3+1.
3. Results 
    - The most relevant architectural views (one to three at most) that you recovered from the analysis of the system
    - Explain the elements in the architectural view(s)
    - ​​[optional] Recommendations for reengineering of the system (did you discover things that seem wrong and should be corrected?)
4. Discussion 
    - What are the limitations of your approach 
      - That I am bound to the use of exisisting tools and their customization is limited to the vision of their creators. That is, if I wanted to seek specific information or a specific view, the existing tools might not be capable of this. In my opinion, the best way to get the information you want from a specific system, would be to make a script that would extract AST from the files and from the AST you can pull the exact information you want. I worked with tree-sitter in my bachelor project, and I believe that it could be used to extract relevant information with regards to the reengineering of a system. 
    - What worked what would you do it better next time?
5. Appendix 
    - Scripts that you wrote or used or (preferable) link to GH repository
    - [optional] Time allocation: how did you spend your time
