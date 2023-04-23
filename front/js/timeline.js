import React from "react";
import { createRoot } from "react-dom/client";
import Timeline from "../components/timeline/Timeline";


(async function () {

    const rootContainer = document.getElementById('container');
    const root = createRoot(rootContainer);

    root.render(<Timeline />);

})();
