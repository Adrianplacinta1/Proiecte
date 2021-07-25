using System;
using System.Collections.Generic;
using System.Text;

namespace Gothic.Shared
{
    class GothicSkill
    {
        public string SkillStat { get; set; } = "";
        public string SkillName { get; set; } = "";

        readonly string BasicCorrector    = "Basic:    ";
        readonly string FairCorrector     = "Fair:     ";
        readonly string AdvancedCorrector = "Advanced: ";
        readonly string ExpertCorrector   = "Expert:   ";
        readonly string MasterCorrector   = "Master:   ";

        public string BasicXP { get; set; } = "";
        public string FairXP { get; set; } = "";
        public string AdvancedXP { get; set; } = "";
        public string ExpertXP { get; set; } = "";
        public string MasterXP { get; set; } = "";

        public string BasicRequirements { get; set; } = "";
        public string FairRequirements { get; set; } = "";
        public string AdvancedRequirements { get; set; } = "";
        public string ExpertRequirements { get; set; } = "";
        public string MasterRequirements { get; set; } = "";



        public string BasicReqirements { get; set; } = "";
        public string FairReqirements { get; set; } = "";
        public string AdvancedReqirements { get; set; } = "";
        public string ExpertReqirements { get; set; } = "";
        public string MasterReqirements { get; set; } = "";

    }
}
