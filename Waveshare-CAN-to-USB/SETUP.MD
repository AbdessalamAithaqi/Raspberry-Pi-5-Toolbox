1. Remove brltty sercive because it incorrectly identifies the device as one of their own and prevemr the ch341 driver from functionning correctly
    ```
    sudo apt remove brltty
    ```
    
2. Install python-can and pyserial library
    ```bash
    pip install python-can pyserial
    ```