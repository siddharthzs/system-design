"""
    Design a distributed key value store which is highly available and is network partition tolerant
    ````````````````````````````````````````````````````````````````````````````````````````````````

    1)Features


    1)Features=>
            Data need to store?
            Support Updates
            Can the size of the value for a key increase with udates?
            Can a value be so big that it does not fit on a single machine
            What is the Estimate QPS for Database?

            Minimum number of machine required to store the data?

    2)Estimation=>
            How scalabel, data which system will required to handle.
            Minimym no. of machine required to store the data?

    3) Design Goals=>
            Latency: Is it is latency sensitive
            Consistency: Tight consistency or okay type
            Availability: 100% availability
    
    4) Deep Dive=>
            Which Type of Database
            Is sharding required?
            How many machine should we shared?
"""