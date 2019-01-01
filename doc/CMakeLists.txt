# Documentation files
set(DOCUMENTATION_FILES main.tex)

# Generate documentation out of LaTeX sources
add_custom_command(Name ALL pdflatex -output-directory${CMAKE_CURRENT_BINARY_DIR} main.tex
	DEPENDS ${DOCUMENTATION_FILES}
	WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
	COMMENT "Generating the documentation"
	SOURCES ${DOCUMENTSTION_FILES})
