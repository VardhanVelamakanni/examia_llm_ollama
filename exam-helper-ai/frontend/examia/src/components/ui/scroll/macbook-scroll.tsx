"use client";

import React, { useEffect, useRef, useState } from "react";
import { MotionValue, motion, useScroll, useTransform } from "motion/react";
import { cn } from "../../../lib/utils";
import {
  IconBrightnessDown,
  IconBrightnessUp,
  IconCaretRightFilled,
  IconCaretUpFilled,
  IconChevronUp,
  IconMicrophone,
  IconMoon,
  IconPlayerSkipForward,
  IconPlayerTrackNext,
  IconPlayerTrackPrev,
  IconTable,
  IconVolume,
  IconVolume2,
  IconVolume3,
  IconSearch,
  IconWorld,
  IconCommand,
  IconCaretLeftFilled,
  IconCaretDownFilled,
} from "@tabler/icons-react";

/* ================================
   MACBOOK SCROLL (MAIN)
================================ */

export const MacbookScroll = ({
  screen,
  showGradient = false,
}: {
  screen?: React.ReactNode;
  showGradient?: boolean;
}) => {
  const ref = useRef<HTMLDivElement>(null);

  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ["start start", "end start"],
  });

  const [isMobile, setIsMobile] = useState(false);

  useEffect(() => {
    if (window.innerWidth < 768) setIsMobile(true);
  }, []);

  const scaleX = useTransform(scrollYProgress, [0, 0.3], [1.2, isMobile ? 1 : 1.5]);
  const scaleY = useTransform(scrollYProgress, [0, 0.3], [0.6, isMobile ? 1 : 1.5]);
  const translate = useTransform(scrollYProgress, [0, 1], [0, 1500]);
  const rotate = useTransform(scrollYProgress, [0.1, 0.12, 0.3], [-28, -28, 0]);

  return (
    <div
      ref={ref}
      className="flex min-h-[200vh] flex-col items-center justify-start [perspective:800px] md:py-80"
    >
      <Lid
        screen={screen}
        scaleX={scaleX}
        scaleY={scaleY}
        rotate={rotate}
        translate={translate}
      />

      {/* BASE */}
      <div className="relative -z-10 h-[22rem] w-[32rem] rounded-2xl bg-[#272729]">
        <div className="relative h-10 w-full">
          <div className="absolute inset-x-0 mx-auto h-4 w-[80%] bg-black" />
        </div>

        <div className="flex">
          <div className="w-[10%]"><SpeakerGrid /></div>
          <div className="w-[80%]"><Keypad /></div>
          <div className="w-[10%]"><SpeakerGrid /></div>
        </div>

        <Trackpad />

        {showGradient && (
          <div className="absolute inset-x-0 bottom-0 h-40 bg-gradient-to-t from-black to-transparent" />
        )}
      </div>
    </div>
  );
};

/* ================================
   LID + SCREEN
================================ */

const Lid = ({
  scaleX,
  scaleY,
  rotate,
  translate,
  screen,
}: {
  scaleX: MotionValue<number>;
  scaleY: MotionValue<number>;
  rotate: MotionValue<number>;
  translate: MotionValue<number>;
  screen?: React.ReactNode;
}) => {
  return (
    <div className="relative [perspective:800px]">
      {/* BACK OF LID */}
      <div
        style={{
          transform: "perspective(800px) rotateX(-25deg)",
          transformOrigin: "bottom",
          transformStyle: "preserve-3d",
        }}
        className="relative h-[12rem] w-[32rem] rounded-2xl bg-black p-2"
      >
        <div className="absolute inset-0 rounded-lg bg-black" />
      </div>

      {/* SCREEN */}
      <motion.div
        style={{
          scaleX,
          scaleY,
          rotateX: rotate,
          translateY: translate,
          transformOrigin: "top",
          transformStyle: "preserve-3d",
        }}
        className="absolute inset-0 h-96 w-[32rem] rounded-2xl bg-black p-2"
      >
        {/* BEZEL */}
        <div className="absolute inset-0 rounded-lg bg-[#272729]" />

        {/* SCREEN CONTENT */}
        <div className="relative z-10 h-full w-full rounded-lg bg-black flex items-center justify-center overflow-hidden">
          {screen}
        </div>
      </motion.div>
    </div>
  );
};

/* ================================
   BASE PARTS
================================ */

const Trackpad = () => (
  <div
    className="mx-auto my-1 h-32 w-[40%] rounded-xl"
    style={{ boxShadow: "0px 0px 1px 1px #00000020 inset" }}
  />
);

const Keypad = () => (
  <div className="mx-1 h-full rounded-md bg-[#050505] p-1">
    {/* First Row */}
    <div className="mb-[2px] flex gap-[2px]">
      <KBtn>esc</KBtn>
      <KBtn><IconBrightnessDown className="h-[6px] w-[6px]" /></KBtn>
      <KBtn><IconBrightnessUp className="h-[6px] w-[6px]" /></KBtn>
      <KBtn><IconTable className="h-[6px] w-[6px]" /></KBtn>
      <KBtn><IconSearch className="h-[6px] w-[6px]" /></KBtn>
      <KBtn><IconMicrophone className="h-[6px] w-[6px]" /></KBtn>
      <KBtn><IconMoon className="h-[6px] w-[6px]" /></KBtn>
      <KBtn><IconPlayerTrackPrev className="h-[6px] w-[6px]" /></KBtn>
      <KBtn><IconPlayerSkipForward className="h-[6px] w-[6px]" /></KBtn>
      <KBtn><IconPlayerTrackNext className="h-[6px] w-[6px]" /></KBtn>
      <KBtn><IconVolume3 className="h-[6px] w-[6px]" /></KBtn>
      <KBtn><IconVolume2 className="h-[6px] w-[6px]" /></KBtn>
      <KBtn><IconVolume className="h-[6px] w-[6px]" /></KBtn>
    </div>
  </div>
);

const KBtn = ({ children }: { children?: React.ReactNode }) => (
  <div className="rounded-[4px] bg-white/[0.2] p-[0.5px]">
    <div className="flex h-6 w-6 items-center justify-center rounded-[3.5px] bg-[#0A090D] text-[6px] text-white">
      {children}
    </div>
  </div>
);

const SpeakerGrid = () => (
  <div
    className="mt-2 h-40"
    style={{
      backgroundImage: "radial-gradient(circle, #08080A 0.5px, transparent 0.5px)",
      backgroundSize: "3px 3px",
    }}
  />
);
