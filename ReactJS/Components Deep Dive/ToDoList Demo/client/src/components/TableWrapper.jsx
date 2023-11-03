import { useState, useEffect } from "react";
import TableItems from "./TableItems";
import * as api from "../Api/GetTasks"


export default function TableWrapper() {
    const [LoadedData, setLoadedData] = useState([])
    

    useEffect( () => {   

        api.GetAllTask()
            .then( result => setLoadedData(result))
            .catch( (result) => console.log(result))
            ;
        
        
    }, []);

    return (

        <div className="table-wrapper">

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
                            teskText = {row.text}
                            isCompleted = {row.isCompleted}
                        />
                    ))
                }
          </tbody>
        </table>
      </div>

    );

}