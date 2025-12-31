import React from "react";
import { EncryptedText } from "../text/encrypted-text";

export function EncryptedTextDemoSecond() {
  return (
    <div className="px-10 text-center">
      <EncryptedText
        text="Welcome to the Matrix, Neo."
        encryptedClassName="text-neutral-500"
        revealedClassName="text-white text-2xl md:text-3xl font-semibold"
        revealDelayMs={40}
      />
    </div>
  );
}
