#!/bin/sh -x
result=`which docker`
if [ -z $result ]; then
        echo "Error: DOCKER command seems not to be present in this OS."
        echo "System defaults are missing.Sorry, Quitting from installation"
        echo "Thank You"
        exit 1
else
   DOCKER=$result
fi
result=`which awk`
if [ -z $result ]; then
        echo "Error: AWK command seems not to be present in this OS."
        echo "System defaults are missing.Sorry, Quitting from installation"
        echo "Thank You"
        exit 1
else
   AWK=$result
fi
result=`which grep`
if [ -z $result ]; then
        echo "Error: grep command seems not to be present in this OS."
        echo "System defaults are missing.Sorry, Quitting from installation"
        echo "Thank You"
        exit 1
else
   GREP=$result
fi
echo -e "\n\n =========== Starting the Docker Clean Up Script ================== \n\n"
echo -e "======= Checking Docker images with imageID as 'None' ======"
noneImages=$($DOCKER images | $GREP -w "<none>" | $AWK '{print $3}')
if [ "${noneImages}" != "" ];then
        for nImages in ${noneImages}
        do
          echo ${nImages}
          ${DOCKER} rmi -f ${nImages} >> cleanUpLog
                if [ $# -eq 0 ]; then
                        echo -n "\n======= Docker image with ImageId: ${nImages} Deleted Successfully =======\n" >> cleanUpLog
                else
                        echo -n "\n======= Error while deleting Docker image with ImageId: ${nImages} =======\n" >> cleanUpLog
                fi
        done
else
        echo "\n====================== [Image ID with <none>]:No Docker Images to delete============ \n"
fi

oldContainers=$($DOCKER ps -a | $GREP "Dead\|Exited" | $AWK '{print $1}')
if [ "$oldContainers" != "" ]; then
  echo ""
        for oContainers in $oldContainers
        do
          echo $j
          $DOCKER rm ${oContainers} >> cleanUpLog
          if [ $# -eq 0 ]; then
                        echo -n "\n ========[Dead|Exited] Docker container with ContainerID: ${oContainers} Deleted Successfully ======= \n" >> cleanUpLog
                else
                        echo -n "\n =======[Dead|Exited] Error while deleting Docker image with COntainedID: ${oContainers} =======\n" >> cleanUpLog
                fi

        done
else
  echo -e "\n ======= There no Docker containers with status as 'Exited' ====== \n" >> cleanUpLog
fi
echo -e "======= Proceeding to next step, removing modelformproject image =============="
docker rmi $(docker images |grep 'modelformproject')
echo -e "\n ======= modelformproject has been successfully deleted ====== \n"
fi

echo -e "\n =============  Clean up unused docker volumes =========================================\n"
unUsedVolumes=$($DOCKER volume ls -qf dangling=true)
if [ "$unUsedVolumes" != "" ]; then
        for uVolumes in ${unUsedVolumes}
        do
                ${DOCKER} rmi -f ${uVolumes} >> cleanUpLog
                if [ $# -eq 0 ]; then
                        echo -n "\n ======= Docker image with ImageId: ${uVolumes} Delted Successfully =======\n" >> cleanUpLog
                else
                        echo -n "\n ======= Error while deleting Docker image with ImageId: ${uVolumes} ======= \n" >> cleanUpLog
                fi
        done
else
        echo -e "\n =================== No Docker dangaling Images to delete ================== \n"
fi

echo -n "\n\n ============================ END OF SCRIPT ============================= \n\n"