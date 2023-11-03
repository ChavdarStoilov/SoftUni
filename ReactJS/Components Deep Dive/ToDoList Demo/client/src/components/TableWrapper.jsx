import { useState, useEffect } from "react";
import TableItems from "./TableItems";
import * as api from "../Api/GetTasks"
import LoadingSpinner from "./LoadingSpinner";


export default function TableWrapper() {
    const [LoadedData, setLoadedData] = useState([])
    const [IsLoading, setIsLoading] = useState(false)

    useEffect( () => {   
        setIsLoading(true)

        api.GetAllTask()
            .then( result => setLoadedData(result))
            .catch( (result) => console.log(result))
            .finally( () => setIsLoading(false))

    }, []);
    // function ChangeStatusTask(id) {

    //     api.UpdateStatus(id)
    //     .then( (result) => console.log(result))

    // }

    return (
        
        <div className="table-wrapper">

        {IsLoading && <LoadingSpinner />}

        <table className="table">
          <thead>
            <tr>
              <th className="table-header-task">Task</th>
              <th className="table-header-status">Status</th>
              <th className="table-header-action">Action</th>
            </tr>
          </thead>
          <tbody>
                {
                    LoadedData.map(row => (
                        <TableItems 
                            key = {row._id}
                            _id={row._id}
                            teskText = {row.text}
                            isCompleted = {row.isCompleted}
                            // ChangeStatusTask
                        />
                    ))
                }
          </tbody>
        </table>
      </div>

    );

}