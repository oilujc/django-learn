import React from "react";
import { createRoot } from "react-dom/client";
import Learning from "../components/learning/Learning";


(async function () {

    const rootContainer = document.getElementById('container');
    const root = createRoot(rootContainer);

    root.render(<Learning current_lesson={rootContainer.dataset.lesson} user_activity_id={rootContainer.dataset.user_activity_id} />);

})();
