#!/bin/bash

cd project/$1

if [[ $? == 0  ]]; then         # Check if cd was successful
    cp -r  ../datastructures ./datastructures
    cp -r  ../resources ./resources
    cp -r  ../customthreads ./customthreads
    cp -r  ../assets ./assets

    DOCKER_IMAGE=$(basename $(pwd))
    [ -z ${docker_image_prefix} ] && { docker_image_prefix="josephkphan/smartmirror"; }

    # Build the docker image
    echo "Building docker image ${docker_image_prefix}/${DOCKER_IMAGE}"
    docker build --no-cache=true -t ${docker_image_prefix}/${DOCKER_IMAGE} .

    echo "Now available docker images for ${docker_image_prefix}/${DOCKER_IMAGE}"
    docker images|grep "${docker_image_prefix}/${DOCKER_IMAGE}"

    rm -r resources datastructures customthreads assets
fi