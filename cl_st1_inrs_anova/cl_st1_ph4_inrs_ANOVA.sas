/* One-Way ANOVA - CL_St1_Ph4_INRS_ANOVA */
/* Replace all occurrences of this project ID by yours and create a folder named after it */
%let project = cl_st1_ph4_inrs_ANOVA;

%let myfolder = &project;

/* Replace all occurrences of this user ID by yours */
%let sasusername = u63529080;

/* Importing the data set */
proc import datafile="/home/&sasusername/&myfolder/debates_turns_parties_scores.tsv"
            out=cl_st1_ph4_inrs_ANOVA
            dbms=tab
            replace;
   getnames=yes;
run;

/* One-Way ANOVA Party Factor 1 */

Title;
ods noproctitle;
ods graphics / imagemap=on;

proc glm data=WORK.CL_ST1_PH4_INRS_ANOVA;
	class Party;
	model 'Factor 1'n=Party;
	means Party / hovtest=bartlett welch plots=none;
	lsmeans Party / adjust=tukey pdiff alpha=.05;
	run;
quit;

/* One-Way ANOVA Party Factor 2 */

Title;
ods noproctitle;
ods graphics / imagemap=on;

proc glm data=WORK.CL_ST1_PH4_INRS_ANOVA;
	class Party;
	model 'Factor 2'n=Party;
	means Party / hovtest=bartlett welch plots=none;
	lsmeans Party / adjust=tukey pdiff alpha=.05;
	run;
quit;

/* One-Way ANOVA Party Factor 3 */

Title;
ods noproctitle;
ods graphics / imagemap=on;

proc glm data=WORK.CL_ST1_PH4_INRS_ANOVA;
	class Party;
	model 'Factor 3'n=Party;
	means Party / hovtest=bartlett welch plots=none;
	lsmeans Party / adjust=tukey pdiff alpha=.05;
	run;
quit;

/* One-Way ANOVA Party Factor 4 */

Title;
ods noproctitle;
ods graphics / imagemap=on;

proc glm data=WORK.CL_ST1_PH4_INRS_ANOVA;
	class Party;
	model 'Factor 4'n=Party;
	means Party / hovtest=bartlett welch plots=none;
	lsmeans Party / adjust=tukey pdiff alpha=.05;
	run;
quit;

/* One-Way ANOVA Party Factor 5 */

Title;
ods noproctitle;
ods graphics / imagemap=on;

proc glm data=WORK.CL_ST1_PH4_INRS_ANOVA;
	class Party;
	model 'Factor 5'n=Party;
	means Party / hovtest=bartlett welch plots=none;
	lsmeans Party / adjust=tukey pdiff alpha=.05;
	run;
quit;

/* One-Way ANOVA Party Factor 6 */

Title;
ods noproctitle;
ods graphics / imagemap=on;

proc glm data=WORK.CL_ST1_PH4_INRS_ANOVA;
	class Party;
	model 'Factor 6'n=Party;
	means Party / hovtest=bartlett welch plots=none;
	lsmeans Party / adjust=tukey pdiff alpha=.05;
	run;
quit;


/* One-Way ANOVA Election Factor 1 */

Title;
ods noproctitle;
ods graphics / imagemap=on;

proc glm data=WORK.CL_ST1_PH4_INRS_ANOVA;
	class Election;
	model 'Factor 1'n=Election;
	means Election / hovtest=bartlett welch plots=none;
	lsmeans Election / adjust=tukey pdiff alpha=.05;
	run;
quit;

/* One-Way ANOVA Election Factor 2 */

Title;
ods noproctitle;
ods graphics / imagemap=on;

proc glm data=WORK.CL_ST1_PH4_INRS_ANOVA;
	class Election;
	model 'Factor 2'n=Election;
	means Election / hovtest=bartlett welch plots=none;
	lsmeans Election / adjust=tukey pdiff alpha=.05;
	run;
quit;

/* One-Way ANOVA Election Factor 3 */

Title;
ods noproctitle;
ods graphics / imagemap=on;

proc glm data=WORK.CL_ST1_PH4_INRS_ANOVA;
	class Election;
	model 'Factor 3'n=Election;
	means Election / hovtest=bartlett welch plots=none;
	lsmeans Election / adjust=tukey pdiff alpha=.05;
	run;
quit;

/* One-Way ANOVA Election Factor 4 */

Title;
ods noproctitle;
ods graphics / imagemap=on;

proc glm data=WORK.CL_ST1_PH4_INRS_ANOVA;
	class Election;
	model 'Factor 4'n=Election;
	means Election / hovtest=bartlett welch plots=none;
	lsmeans Election / adjust=tukey pdiff alpha=.05;
	run;
quit;

/* One-Way ANOVA Election Factor 5 */

Title;
ods noproctitle;
ods graphics / imagemap=on;

proc glm data=WORK.CL_ST1_PH4_INRS_ANOVA;
	class Election;
	model 'Factor 5'n=Election;
	means Election / hovtest=bartlett welch plots=none;
	lsmeans Election / adjust=tukey pdiff alpha=.05;
	run;
quit;

/* One-Way ANOVA Election Factor 6 */

Title;
ods noproctitle;
ods graphics / imagemap=on;

proc glm data=WORK.CL_ST1_PH4_INRS_ANOVA;
	class Election;
	model 'Factor 6'n=Election;
	means Election / hovtest=bartlett welch plots=none;
	lsmeans Election / adjust=tukey pdiff alpha=.05;
	run;
quit;
