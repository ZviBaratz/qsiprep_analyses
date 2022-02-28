from pathlib import Path
from typing import Union

import bids

from qsiprep_analyses.data.bids import DEFAULT_PATH_PATTERNS


class DataGrabber:
    #: Templates
    SUBJECT_TEMPLATE = "sub-"
    SESSION_TEMPLATE = "ses-"
    PATH_PATTERNS = DEFAULT_PATH_PATTERNS

    def __init__(self, base_dir: Path, generate_layout: bool = True) -> None:
        self.base_dir = Path(base_dir)
        if generate_layout:
            self.layout = self.get_bids_layout()

    def get_bids_layout(self) -> bids.BIDSLayout:
        """
        Return a pybids' layout of *self.base_dir*

        Returns
        -------
        bids.BIDSLayout
            A pybids' layout of *self.base_dir*
        """
        return bids.BIDSLayout(self.base_dir, derivatives=True, validate=False)

    def query_subjects(self) -> dict:
        """
        Queries a derivatives' directory and locates all available subjects and their corresponding sessions

        Returns
        -------
        dict
            A dictionary with participant labels as keys and available sessions as values
        """
        subjects = {
            subj.name.replace(self.SUBJECT_TEMPLATE, ""): [
                ses.name.replace(self.SESSION_TEMPLATE, "")
                for ses in sorted(
                    self.base_dir.glob(f"{subj.name}/{self.SESSION_TEMPLATE}*")
                )
            ]
            for subj in sorted(self.base_dir.glob(f"{self.SUBJECT_TEMPLATE}*"))
            if subj.is_dir()
        }
        return subjects

    def build_path(
        self, source: Union[dict, str, Path], replacements: dict
    ) -> Path:
        """
        Build a BIDS-compatible path according to source file/entities.

        Parameters
        ----------
        source : Union[dict, str, Path]
            Either a source file (to be parsed to entities) or its BIDS entities.
        replacements : dict
            A dictionary with keys as entities and values as replacement/addition values.

        Returns
        -------
        Path
            Path to BIDS-compatible path
        """
        if isinstance(source, (str, Path)):
            source = bids.layout.parse_file_entities(source)
        for key, value in replacements.items():
            source[key] = value
        return Path(
            self.layout.build_path(
                source,
                path_patterns=self.PATH_PATTERNS,
                validate=False,
                strict=True,
            )
        )

    @property
    def subjects(self) -> dict:
        return self.query_subjects()
