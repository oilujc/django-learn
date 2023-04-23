import React from "react";
import { createRoot } from "react-dom/client";

import SetInterests from '../components/interest/SetInterests';


(async function () {

    const rootContainer = document.getElementById('container');
    const root = createRoot(rootContainer);

    root.render(<SetInterests />);

})();
