"use client";

import React from "react";
import { MacbookScroll } from "./macbook-scroll";
import { EncryptedTextDemoSecond } from "../../ui/text/encrypted-demo";

export function MacbookScrollDemo() {
  return (
    <div className="w-full overflow-hidden bg-white dark:bg-[#0B0B0F]">
      <MacbookScroll
        screen={<EncryptedTextDemoSecond />}
        showGradient={false}
      />
    </div>
  );
}
