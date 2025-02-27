from pathlib import Path

BIDS_CONFIGURATION_FILE = (
    Path(__file__).parent / "derivatives.json"
).absolute()
DEFAULT_PATH_PATTERNS = [
    "sub-{subject}[/ses-{session}]/{datatype<anat>|anat}/sub-{subject}[_ses-{session}][_acq-{acquisition}][_ce-{ceagent}][_rec-{reconstruction}][_space-{space}][_res-{resolution}][_part-{part}]_{suffix<T1w|T2w|T1rho|T1map|T2map|T2star|FLAIR|FLASH|PDmap|PD|PDT2|inplaneT[12]|angio>}{extension<.nii|.nii.gz|.json>|.nii.gz}",
    "sub-{subject}[/ses-{session}]/{datatype<anat>|anat}/sub-{subject}[_ses-{session}][_acq-{acquisition}][_ce-{ceagent}][_rec-{reconstruction}][_space-{space}][_res-{resolution}][_mod-{modality}]_{suffix<defacemask>}{extension<.nii|.nii.gz|.json>|.nii.gz}",
    "sub-{subject}[/ses-{session}]/{datatype<dwi>|dwi}/sub-{subject}[_ses-{session}][_acq-{acquisition}][_dir-{direction}][_space-{space}][_res-{resolution}][_desc-{desc}][_part-{part}]_{suffix<dwi|dwiref|epiref>}{extension<.bval|.bvec|.json|.nii.gz|.nii>|.nii.gz}",
    "sub-{subject}[/ses-{session}]/{datatype<dwi>|dwi}/sub-{subject}[_ses-{session}][_acq-{acquisition}][_dir-{direction}][_space-{space}][_res-{resolution}][_desc-{desc}][_part-{part}]_{suffix<dwi|dwiref|epiref|mask>}{extension<.bval|.bvec|.json|.nii.gz|.nii>|.nii.gz}",
    "sub-{subject}[/ses-{session}]/{datatype<dwi>|dwi}/sub-{subject}[_ses-{session}][_acq-{acquisition}][_dir-{direction}][_space-{space}][_label-{label}][_res-{resolution}][_desc-{desc}][_atlas-{atlas}]_{suffix<dseg>}{extension<.csv|.pickle|.tsv|.json>|.pickle}",
    "sub-{subject}[/ses-{session}]/{datatype<fmap>|fmap}/sub-{subject}[_ses-{session}][_acq-{acquisition}][_dir-{direction}][_run-{run}]_{fmap<phasediff|magnitude[12]|phase[12]|fieldmap>}{extension<.nii|.nii.gz|.json>|.nii.gz}",
    "sub-{subject}[/ses-{session}]/{datatype<fmap>|fmap}/sub-{subject}[_ses-{session}][_acq-{acquisition}][_ce-{ceagent}]_dir-{direction}[_run-{run}]_{fmap<epi>}{extension<.nii|.nii.gz|.json>|.nii.gz}",
    "[acq-{acquisition}_][ce-{ceagent}_][rec-{reconstruction}_]{suffix<T1w|T2w|T1rho|T1map|T2map|T2star|FLAIR|FLASH|PDmap|PD|PDT2|inplaneT[12]|angio>}{extension<.json>|.json}",
    "[acq-{acquisition}_][ce-{ceagent}_][rec-{reconstruction}_][mod-{modality}_]{suffix<defacemask>}{extension<.json>|.json}",
    "task-{task}[_acq-{acquisition}][_ce-{ceagent}][_dir-{direction}][_rec-{reconstruction}][_run-{run}][_echo-{echo}]_{suffix<bold|cbv|phase|sbref>}{extension<.json>|.json}",
    "[acq-{acquisition}_]{suffix<dwi>}{extension<.json>|.json}",
    "[acq-{acquisition}_][dir-{direction}_][run-{run}_]{fmap<phasediff|magnitude[1-2]|phase[1-2]|fieldmap>}{extension<.json>|.json}",
    "[acq-{acquisition}_][ce-{ceagent}_]dir-{direction}[_run-{run}]_{fmap<epi>}{extension<.json>|.json}",
    "task-{task}[_acq-{acquisition}][_rec-{reconstruction}][_run-{run}][_echo-{echo}][_recording-{recording}]_{suffix<events>}{extension<.json>|.json}",
    "task-{task}[_acq-{acquisition}][_rec-{reconstruction}][_run-{run}][_echo-{echo}][_recording-{recording}]_{suffix<physio|stim>}{extension<.json>}",
]

# flake8: noqa: E501
