CMAKE_MINIMUM_REQUIRED(VERSION 3.0)
PROJECT(tk_config_default2)

include(ExternalProject)

# We check if we are using either the Rez build system, or if we are doing a pure CMake build.
# If the former, we are making use of the Rez dedicated environment variables.
# If the latter, we rely on environment or local variables that we define ourselves.
if(DEFINED ENV{REZ_BUILD_ENV})
    message("\n[CMAKE][SETUP] The project build will be done through Rez.\n")

    include(RezBuild)
    set(PROJECT_VERSION $ENV{REZ_BUILD_PROJECT_VERSION})
    set(INSTALL_PATH $ENV{REZ_BUILD_INSTALL_PATH})
    set(ARCHIVE_PATH $ENV{REZ_REPO_PAYLOAD_DIR})
    # The environment variable REZ_TMP_PATH is meant to point to a location such as "/tmp/rez".
    set(TMP_PATH $ENV{REZ_TMP_PATH})
    set(BUILD_THREADS $ENV{REZ_BUILD_THREAD_COUNT})
else()
    message("\n[CMAKE][SETUP] The project build will be done through pure CMake.\n")

    include(ProcessorCount)

    set(PROJECT_VERSION 1.2.10)
    set(INSTALL_PATH ${CMAKE_INSTALL_PREFIX}/${CMAKE_PROJECT_NAME}/${PROJECT_VERSION})
    set(ARCHIVE_PATH $ENV{BUILD_ARCHIVE_PATH})
    set(TMP_PATH $ENV{BUILD_TMP_PATH})
    ProcessorCount(BUILD_THREADS)
endif()

# We build the path to the archive of the project we are building.
set(ARCHIVE_URL ${ARCHIVE_PATH}/tk_config_default2/tk-config-default2-${PROJECT_VERSION}.tar.gz)

if(NOT EXISTS ${ARCHIVE_URL})
    message(FATAL_ERROR "Archive not found, using the following path: ${ARCHIVE_URL}. "
    "Either the path leading to it is wrong, or it does not exist. If the archive does not indeed exist, "
    "please consider using the following link to download it: "
    "https://github.com/shotgunsoftware/tk-config-default2/archive/v${PROJECT_VERSION}.tar.gz")
endif()

set(EXTRACT_PATH ${TMP_PATH}/${CMAKE_PROJECT_NAME}/${PROJECT_VERSION})

install(
    CODE
    "execute_process(
        COMMAND bash ${CMAKE_SOURCE_DIR}/install.sh ${EXTRACT_PATH} ${INSTALL_PATH} ${PROJECT_VERSION} ${ARCHIVE_URL}
        RESULT_VARIABLE RETURN_CODE_INSTALL
    )
    if (NOT RETURN_CODE_INSTALL EQUAL \"0\")
        message(FATAL_ERROR \"[CMAKE] Install script returned an error code. Aborting...\")
    endif()"
)
