cmake_minimum_required(VERSION 3.0)

add_executable(makesoftcore makesoftcore.c
	${CMAKE_CURRENT_SOURCE_DIR}/../src/lzcompress.c
	${CMAKE_CURRENT_SOURCE_DIR}/../src/bit.c)
target_compile_definitions(makesoftcore PUBLIC -DFICL_WANT_LZ_SOFTCORE=0 -DFICL_WANT_LOCALS=1 -DFICL_WANT_USER=1)
target_include_directories(makesoftcore PRIVATE "${CMAKE_CURRENT_SOURCE_DIR}/../src" "${CMAKE_CURRENT_SOURCE_DIR}/..")
set_property(TARGET makesoftcore PROPERTY POSITION_INDEPENDENT_CODE ON)

# FORTH-defined software words image for FICL.
set(softwords
	softcore.fr
	ifbrack.fr
	prefix.fr
	ficl.fr
	jhlocal.fr
	marker.fr
	oo.fr
	classes.fr
	string.fr
	ficllocal.fr
	fileaccess.fr)

if(WIN32)
	list(APPEND softwords win32.fr)
endif()

# Generate softcore.c for ficl.
add_custom_command(TARGET makesoftcore
	POST_BUILD
	WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
	COMMAND "${CMAKE_CURRENT_BINARY_DIR}/makesoftcore" ${softwords}
	COMMENT "Generating softcore.c for FICL")

